#vmd -dispdev text -e DistanceMeasure.tcl -args GFD3_single_QM_mopac_QwikMD QMMM SingleDistance 1 1 1
#vmd -dispdev text -e $argv0 -args input_psf intput_trajectory output NumberOfPeptide_X NumberOfPeptide_Y NumberOfPeptide_Z
package require timeline 2.3
package require topotools 1.7

set psf [lindex $argv 0]
set trajectory [lindex $argv 1]
set outputfile [lindex $argv 2]
set pepx [lindex $argv 3]
set pepy [lindex $argv 4]
set pepz [lindex $argv 5]
set NumberOfPep [expr $pepx*$pepy*$pepz]
set NumberOfQM [expr $pepx*$pepy*$pepz*3]
set BaseSelectionNumbers { 14 46 78 }
set QMregions {}
mol new ${psf}.psf
mol addfile ${trajectory}.dcd type dcd first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all

#Generating atomselections
for {set i 0} {$i<$NumberOfPep} {incr i} {
  for {set j 0} {$j<3} {incr j} {
    set QM [atomselect top "serial [expr [lindex $BaseSelectionNumbers $j]+$i*103] to [expr [lindex $BaseSelectionNumbers $j]+13+$i*103]" ]
    lappend QMregions $QM
  }
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
      #if {$j != $k } {
          #This calculates the distance between the center-of-mass of two groups ofatoms
          set distance [veclength [vecsub [measure center [lindex $QMregions $j] weight mass] [measure center [lindex $QMregions $k] weight mass] ] ]
          append line $distance ","
      #    }
      }
  }

  #Write the frame number and distance to file, separated by a tabulator
  puts $output "$line"
  }

#Close and clean up everything
#$QMregions delete
unset numframes
unset output
