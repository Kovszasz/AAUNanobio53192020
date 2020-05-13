#vmd -dispdev text -e AngleMeasure.tcl -args GFD3_single_QM_mopac_QwikMD QMMM SingleAngle 1 1 1
#vmd -dispdev text -e $argv0 -args input_psf intput_trajectory output NumberOfPeptide_X NumberOfPeptide_Y NumberOfPeptide_Z
package require timeline 2.3
package require topotools 1.7
package require math
proc CreatePlane {points} {
  set line1 [list [expr [lindex $points 0 0 0] - [lindex $points 1 0 0]] [expr [lindex $points 0 0 1] - [lindex $points 1 0 1]] [expr [lindex $points 0 0 2] - [lindex $points 1 0 2]]]
  set line2 [list [expr [lindex $points 0 0 0] - [lindex $points 2 0 0]] [expr [lindex $points 0 0 1] - [lindex $points 2 0 1]] [expr [lindex $points 0 0 2] - [lindex $points 2 0 2]]]
  set r [list [expr [lindex $line1 1]*[lindex $line2 2]-[lindex $line1 2]*[lindex $line2 1]] [expr [lindex $line1 2]*[lindex $line2 0]-[lindex $line1 0]*[lindex $line2 2]] [expr [lindex $line1 0]*[lindex $line2 1]-[lindex $line1 1]*[lindex $line2 0]]]
  return $r
}

proc CalculateAngle {plane1 plane2} {
  set a [expr abs([lindex $plane1 0]*[lindex $plane2 0] + [lindex $plane1 1]*[lindex $plane2 1] + [lindex $plane1 2]*[lindex $plane2 2])]
  set b [expr sqrt( [lindex $plane1 0]*[lindex $plane1 0] + [lindex $plane1 1]*[lindex $plane1 1]+[lindex $plane1 2]*[lindex $plane1 2])*sqrt([lindex $plane2 0]*[lindex $plane2 0] +[lindex $plane2 1]*[lindex $plane2 1]+[lindex $plane2 2]*[lindex $plane2 2])]
  set A [expr $a/$b]
  return $A
}


set psf [lindex $argv 0]
set trajectory [lindex $argv 1]
set outputfile [lindex $argv 2]
set pepx [lindex $argv 3]
set pepy [lindex $argv 4]
set pepz [lindex $argv 5]
set NumberOfPep [expr $pepx*$pepy*$pepz]
set NumberOfQM [expr $pepx*$pepy*$pepz*3]
set BaseSelectionNumbers { 14 46 78 }
mol new ${psf}.psf
mol addfile ${trajectory}.dcd type dcd first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all

#Generating atomselections
proc get_PlanePoints {NumberOfPep BaseSelectionNumbers} {
  set returnlist {}
  for {set i 0} {$i<$NumberOfPep} {incr i} {
    for {set j 0} {$j<3} {incr j} {
      set pl {}
      for {set k 0} {$k<3} {incr k} {
        set point [atomselect top "serial [expr [lindex $BaseSelectionNumbers $j]+$k*4+$i*103] to [expr [lindex $BaseSelectionNumbers $j]+$k*4+$i*103]" ]
        lappend pl [$point get {x y z}]
        }
        set planes [CreatePlane $pl]
        lappend returnlist $planes
        }
    }
    return $returnlist
}

#Get number of frames loaded into top molecule
set numframes [molinfo top get numframes]

#Open file for writing output
set output [open "${outputfile}.dat" w]

#Loop over all frames
for {set i 0} {$i < $numframes} {incr i} {
  set line "$i"
  animate goto $i
  for {set j 0} {$j < $NumberOfQM} {incr j} {
    append line ";"
    for {set k 0} {$k <$NumberOfQM} {incr k} {
          set PlanePoints [get_PlanePoints $NumberOfPep $BaseSelectionNumbers]
          set angle [CalculateAngle [lindex $PlanePoints $j] [lindex $PlanePoints $k]]
          append line $angle ","
      }
  }
  puts $output "$line"
  }

#Close and clean up everything
#$QMregions delete
unset numframes
unset output
