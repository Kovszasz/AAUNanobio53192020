#Usage: vmd -dispdev text -e $argv0 -args distance_y distance_z NumberOfPeptide_X NumberOfPeptide_Y NumberOfPeptide_Z inputfile outputfile

package require topotools 1.7
set distance_y [lindex $argv 0]
set distance_z [lindex $argv 1]
set x [lindex $argv 2]
set y [lindex $argv 3]
set z [lindex $argv 4]
set inputfile [lindex $argv 5]
set outputfile [lindex $argv 6]
set sellist {}
set elementCoord {0.0 0.0 0.0}
set chainlist {{"A" "B" "C"} {"D" "E" "F"}}
for {set i 0} {$i<$x } {incr i} {
    for {set j 0} {$j<$y } {incr j} {
        for {set k 0} {$k<$z } {incr k} {
            set mol [mol new ${inputfile}.psf waitfor all]
            mol addfile ${inputfile}.pdb
            set newchain "A$i$j$k"
            puts "$newchain"
	    #if {$j==1} {
		#$mol set chain "B"	
	    #}
	    #if {$j==2} {
	    #	$mol set chain "C"
  	    #}
            #$mol set chain $newchain
            #$mol set segid $newchain
            set sel [atomselect $mol protein]
            $sel set chain [lindex $chainlist $k $j]
            $sel set segid $newchain
            set move_x $distance_y*$i
            set move_y $distance_y*$j
            set move_z $distance_z*$k
            set l [expr $j%2]
	    set l2 [expr $k%2]
	    puts "rotation: $l"
            if {$l==0} {
              set sel [atomselect $mol protein]
              set com [measure center $sel weight mass]
              set matrix [transaxis z 180]
              $sel moveby [vecscale -1.0 $com]
              $sel move $matrix
              $sel moveby $com
	      #set move_z [expr $move_z-6.3]
	      #set move_x [expr $move_x-1]
            }
	    if {$l2==0} {
	      set sel [atomselect $mol protein]
              set com [measure center $sel weight mass]
              set matrix [transaxis y 180]
              $sel moveby [vecscale -1.0 $com]
              $sel move $matrix
              $sel moveby $com
	      #set move_z [expr $move_z-6.3]
	      #set move_x [expr $move_x-1]
 	    }
            set translation [list [expr [lindex $elementCoord 0] + $move_x] [expr [lindex $elementCoord 1] + $move_y] [expr [lindex $elementCoord 2] + $move_z]]
            $sel moveby $translation
            lappend sellist $sel
}
}
}
#set mol [mol new GFD3.psf waitfor all]
#mol addfile GFD3.pdb


#set sel [atomselect 1 protein]
#lappend sellist $sel
# do the magic
set mol [::TopoTools::selections2mol $sellist]
animate write psf ${outputfile}.psf $mol
animate write pdb ${outputfile}.pdb $mol



#package require topotools 1.7

#set mol [mol new GFD3.psf waitfor all]
#mol addfile GFD3.pdb

#set sellist {}
#for {set i 0} {$i<4 } {incr i}{
#    set sel [atomselect top protein]
 #   $sel moveby {[expr 50.0*$i] 0.0 0.0}
  #  lappend sellist $sel
#}
#set sel [atomselect top "same residue as (within 3.0 of chain L)"]
#lappend sellist $sel
# do the magic
#set mol [::TopoTools::selections2mol $sellist]
#animate write psf GFD3multimer.psf $mol
#animate write pdb GFD3multimer.pdb $mol

