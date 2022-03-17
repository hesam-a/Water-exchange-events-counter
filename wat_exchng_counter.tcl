
# vmd script for selecting the oxygens around the first coordination shell
# of atom of interest 

# define the distance cuttoff which should be the first coordination shell
# and can be found out with plotting the radial distribution function.
set dist_cutoff 3.5

# define the atom selection around your atom of interest 
set oxygen_sel [atomselect 0 "(oxygen within $dist_cutoff of name Sm2)"]

# get the number of frames
set total_frames [molinfo 0 get numframes]

puts "Number of frames: $total_frames "
puts "Index of Oxygen"

for { set frame_num 0 } { $frame_num < $total_frames } { incr frame_num } {

    $oxygen_sel frame $frame_num
    $oxygen_sel update

    # get the oxygen indices availble in the first coordination shell of your atom of interest
    puts " [$oxygen_sel  get index] "

}

exit
