def binary(key, value):
    if value == '0' or value == '1':
        return 'ok'
    else:
        return "Invalid value: '%s' for '%s', must be 1 or 0" % (value, key)


def constant(key, value):
    return "You can\'t change this setting: '%s'" % key


def free(key, value):
    return 'ok'


def ignore(key, value):
    return 'ignore'


def percentage(key, value, start=0, end=100):
    tmp_value = value.rstrip('%')
    return int_range(key, tmp_value, start, end)


def float_range(key, value, start=float('-inf'), end=float('inf')):
    try:
        tmp_value = float(value)
    except:
        return "Invalid value: '%s', must be a float" % value
    else:
        if start <= tmp_value and tmp_value <= end:
            return 'ok'
        else:
            return "Invalid value: %s for '%s', must be within [%f-%f]" % (value, key, start, end)


def int_range(key, value, start=float('-inf'), end=float('inf')):
    try:
        tmp_value = int(value)
    except:
        return "Invalid value: '%s' for '%s', must be a integer" % (value, key)
    else:
        if start <= tmp_value and tmp_value <= end:
            return 'ok'
        else:
            return "Invalid value: '%s' for '%s', must be within [%d-%d]" % (value, key, start, end)


def finite_choice(key, value, white_list):
    if value in white_list:
        return 'ok'
    else:
        return "Invalid value: '%s' for '%s', must be one of %s" % (value, key, repr(white_list)[1:-1])


def hex_color(key, value):
    value = value.upper()
    try:
        assert value[1] != '#'
        value = value.lstrip('#')
        assert len(value) == 6
        if all(j <= 255 for j in [int(value[i:i + len(value) // 3], 16) for i in range(0, len(value), len(value) // 3)]):
            return 'ok'
        else:
            raise
    except:
        return "Invalid value: '%s' for %s, must be a hex color" % (value, key)


def float_or_percent(key, value, percent_start=float('-inf'), percent_end=float('inf'), float_start=float('-inf'), float_end=float('inf')):
    m = "Invalid value: '%s' for '%s', must be float or percentage" % (value, key)

    try:
        if value.endswith('%'):
            v = float(value[:-1])
            if v >= percent_start and v <= percent_end:
                m = 'ok'
        else:
            if float(value) >= float_start and float(value) <= float_end:
                m = 'ok'
    except:
        pass
    finally:
        return m


ini_string = """# generated by Slic3r 1.2.9 on Tue Nov 10 23:28:47 2015
avoid_crossing_perimeters = 0
bed_shape = 84.5344x8.88492,83.1425x17.6725,80.8398x26.2664,77.6514x34.5726,73.6122x42.5,68.7664x49.9617,63.1673x56.8761,56.8761x63.1673,49.9617x68.7664,42.5x73.6122,34.5726x77.6514,26.2664x80.8398,17.6725x83.1425,8.88492x84.5344,0x85,-8.88492x84.5344,-17.6725x83.1425,-26.2664x80.8398,-34.5726x77.6514,-42.5x73.6122,-49.9617x68.7664,-56.8761x63.1673,-63.1673x56.8761,-68.7664x49.9617,-73.6122x42.5,-77.6514x34.5726,-80.8398x26.2664,-83.1425x17.6725,-84.5344x8.88492,-85x0,-84.5344x-8.88492,-83.1425x-17.6725,-80.8398x-26.2664,-77.6514x-34.5726,-73.6122x-42.5,-68.7664x-49.9617,-63.1673x-56.8761,-56.8761x-63.1673,-49.9617x-68.7664,-42.5x-73.6122,-34.5726x-77.6514,-26.2664x-80.8398,-17.6725x-83.1425,-8.88492x-84.5344,0x-85,8.88492x-84.5344,17.6725x-83.1425,26.2664x-80.8398,34.5726x-77.6514,42.5x-73.6122,49.9617x-68.7664,56.8761x-63.1673,63.1673x-56.8761,68.7664x-49.9617,73.6122x-42.5,77.6514x-34.5726,80.8398x-26.2664,83.1425x-17.6725,84.5344x-8.88492,85x0
bed_temperature = 0
before_layer_gcode =
bottom_solid_layers = 3
bridge_acceleration = 0
bridge_fan_speed = 100
bridge_flow_ratio = 1
bridge_speed = 20
brim_width = 0
complete_objects = 0
cooling = 1
default_acceleration = 0
disable_fan_first_layers = 5
dont_support_bridges = 1
duplicate_distance = 6
end_gcode = M104 S0 ; turn off temperature\\nG91\\nG1 E-1 F300\\nG1 Z+5 E-5 F9000\\nG28 X0  ; home X axis\\nM84     ; disable motors\\n
external_fill_pattern = rectilinear
external_perimeter_extrusion_width = 0.4
external_perimeter_speed = 70%
external_perimeters_first = 0
extra_perimeters = 1
extruder_clearance_height = 20
extruder_clearance_radius = 20
extruder_offset = 0x0
extrusion_axis = E
extrusion_multiplier = 1
extrusion_width = 0.4
fan_always_on = 0
fan_below_layer_time = 15
filament_colour = #FFFFFF
filament_diameter = 1.75
fill_angle = 45
fill_density = 20%
fill_pattern = honeycomb
first_layer_acceleration = 0
first_layer_bed_temperature = 0
first_layer_extrusion_width = 120%
first_layer_height = 0.35
first_layer_speed = 20
first_layer_temperature = 220
gap_fill_speed = 20
gcode_arcs = 0
gcode_comments = 0
gcode_flavor = reprap
geometric_error_correction_on = 1
infill_acceleration = 0
infill_every_layers = 1
infill_extruder = 1
infill_extrusion_width = 0.4
infill_first = 0
infill_only_where_needed = 0
infill_overlap = 15%
infill_speed = 50
interface_shells = 0
layer_gcode =
layer_height = 0.2
max_fan_speed = 100
max_print_speed = 50
max_volumetric_speed = 0
min_fan_speed = 80
min_print_speed = 3
min_skirt_length = 0
notes =
nozzle_diameter = 0.4
octoprint_apikey =
octoprint_host =
only_retract_when_crossing_perimeters = 1
ooze_prevention = 0
output_filename_format = [input_filename_base].gcode
overhangs = 0
perimeter_acceleration = 0
perimeter_extruder = 1
perimeter_extrusion_width = 0.4
perimeter_speed = 30
perimeters = 3
post_process =
pressure_advance = 0
raft = 1
raft_layers = 0
resolution = 0.01
retract_before_travel = 2
retract_layer_change = 0
retract_length = 5.5
retract_length_toolchange = 10
retract_lift = 0.1
retract_restart_extra = 0
retract_restart_extra_toolchange = 0
retract_speed = 60
seam_position = aligned
skirt_distance = 20
skirt_height = 1
skirts = 1
slowdown_below_layer_time = 15
small_perimeter_speed = 15
solid_infill_below_area = 70
solid_infill_every_layers = 0
solid_infill_extruder = 1
solid_infill_extrusion_width = 0.4
solid_infill_speed = 20
spiral_vase = 0
standby_temperature_delta = -5
start_gcode = G1 Z5 F5000 ; lift nozzle\\n
support_material = 1
support_material_angle = 0
support_material_contact_distance = 0.2
support_material_enforce_layers = 0
support_material_extruder = 1
support_material_extrusion_width = 0.4
support_material_interface_extruder = 1
support_material_interface_layers = 3
support_material_interface_spacing = 0
support_material_interface_speed = 100%
support_material_pattern = rectilinear-grid
support_material_spacing = 2
support_material_speed = 40
support_material_threshold = 55
temperature = 210
thin_walls = 0
threads = 2
toolchange_gcode =
top_infill_extrusion_width = 0.4
top_solid_infill_speed = 15
top_solid_layers = 4
travel_speed = 80
use_firmware_retraction = 0
use_relative_e_distances = 0
use_volumetric_e = 0
vibration_limit = 0
wipe = 0
xy_size_compensation = 0
z_offset = 0
flux_refill_empty = 0
flux_first_layer = 0
flux_raft = 0
cut_bottom = -1
detect_filament_runout = 1
detect_head_shake = 1
detect_head_tilt = 1
flux_calibration = 1
pause_at_layers =
support_everywhere = 0
cura2 = 0"""

ini_string_cura2 = """machine_start_gcode = G28
machine_end_gcode = 
material_bed_temp_wait = true
material_print_temp_wait = true
material_print_temp_prepend = true
material_bed_temp_prepend = true
machine_heated_bed = false
machine_extruder_count = 1
machine_min_cool_heat_time_window = 50
machine_disallowed_areas = 
nozzle_disallowed_areas = 
machine_nozzle_size = 0.4
extruder_prime_pos_z = 0
extruder_prime_pos_abs = false
layer_height = 0.1
layer_height_0 = 0.3
wall_line_width_0 = 0.4
wall_line_width_x = 0.4
skin_line_width = 0.4
infill_line_width = 0.4
skirt_brim_line_width = 0.4
support_line_width = 0.4
support_interface_line_width = 0.4
prime_tower_line_width = 0.4
wall_line_count = 2
wall_0_wipe_dist = 0.2
top_layers = 8
bottom_layers = 6
top_bottom_pattern = lines
top_bottom_pattern_0 = lines
wall_0_inset = 0
outer_inset_first = false
alternate_extra_perimeter = false
travel_compensate_overlapping_walls_0_enabled = true
travel_compensate_overlapping_walls_x_enabled = true
fill_perimeter_gaps = everywhere
xy_offset = 0
z_seam_type = shortest
z_seam_x = 100
z_seam_y = 100
skin_no_small_gaps_heuristic = true
infill_line_distance = 2
infill_pattern = zigzag
sub_div_rad_mult = 100
sub_div_rad_add = 0.4
infill_overlap_mm = 0.04
skin_overlap_mm = 0.02
infill_wipe_dist = 0.04
infill_sparse_thickness = 0.1
gradual_infill_steps = 0
gradual_infill_step_height = 5
infill_before_walls = true
min_infill_area = 0
material_flow_dependent_temperature = false
default_material_print_temperature = 210
material_print_temperature = 210
material_print_temperature_layer_0 = 215
material_initial_print_temperature = 200
material_final_print_temperature = 195
material_flow_temp_graph = [[3.5,200],[7.0,240]]
material_extrusion_cool_down_speed = 0.7
material_bed_temperature = 60
material_bed_temperature_layer_0 = 60
material_diameter = 2.85
material_flow = 100
retraction_enable = true
retract_at_layer_change = false
retraction_amount = 6.5
retraction_retract_speed = 25
retraction_prime_speed = 25
retraction_extra_prime_amount = 0
retraction_min_travel = 1.5
retraction_count_max = 90
retraction_extrusion_window = 4.5
material_standby_temperature = 150
switch_extruder_retraction_amount = 20
switch_extruder_retraction_speed = 20
switch_extruder_prime_speed = 20
speed_infill = 60
speed_wall_0 = 30
speed_wall_x = 60
speed_topbottom = 30
speed_support_infill = 60
speed_support_interface = 40
speed_prime_tower = 60
speed_travel = 120
speed_print_layer_0 = 30
speed_travel_layer_0 = 60
skirt_brim_speed = 30
max_feedrate_z_override = 0
speed_slowdown_layers = 2
speed_equalize_flow_enabled = false
speed_equalize_flow_max = 150
acceleration_enabled = false
acceleration_infill = 3000
acceleration_wall_0 = 3000
acceleration_wall_x = 3000
acceleration_topbottom = 3000
acceleration_support_infill = 3000
acceleration_support_interface = 3000
acceleration_prime_tower = 3000
acceleration_travel = 5000
acceleration_print_layer_0 = 3000
acceleration_travel_layer_0 = 3000
acceleration_skirt_brim = 3000
jerk_enabled = false
jerk_infill = 20
jerk_wall_0 = 20
jerk_wall_x = 20
jerk_topbottom = 20
jerk_support_infill = 20
jerk_support_interface = 20
jerk_prime_tower = 20
jerk_travel = 30
jerk_print_layer_0 = 20
jerk_travel_layer_0 = 20
jerk_skirt_brim = 20
retraction_combing = all
travel_avoid_other_parts = true
travel_avoid_distance = 0.625
start_layers_at_same_position = false
layer_start_x = 0
layer_start_y = 0
retraction_hop_enabled = true
retraction_hop_only_when_collides = false
retraction_hop = 1
retraction_hop_after_extruder_switch = true
cool_fan_enabled = true
cool_fan_speed_min = 100
cool_fan_speed_max = 100
cool_min_layer_time_fan_speed_max = 10
cool_fan_speed_0 = 0
cool_fan_full_layer = 2
cool_min_layer_time = 5
cool_min_speed = 10
cool_lift_head = false
support_enable = false
support_infill_extruder_nr = 0
support_extruder_nr_layer_0 = 0
support_interface_extruder_nr = 0
support_type = everywhere
support_angle = 50
support_pattern = zigzag
support_connect_zigzags = true
support_line_distance = 1.75
support_top_distance = 0.1
support_bottom_distance = 0.1
support_xy_distance = 0.7
support_xy_overrides_z = z_overrides_xy
support_xy_distance_overhang = 0.2
support_bottom_stair_step_height = 0.3
support_join_distance = 2
support_offset = 0.2
support_interface_enable = false
support_roof_height = 1
support_bottom_height = 1
support_interface_skip_height = 0.3
support_interface_line_distance = 0.4
support_interface_pattern = concentric
support_use_towers = true
support_tower_diameter = 3
support_minimal_diameter = 3
support_tower_roof_angle = 65
extruder_prime_pos_x = 0
extruder_prime_pos_y = 0
adhesion_type = brim
adhesion_extruder_nr = 0
skirt_line_count = 1
skirt_gap = 3
skirt_brim_minimal_length = 250
brim_line_count = 20
brim_outside_only = true
raft_margin = 15
raft_airgap = 0.3
layer_0_z_overlap = 0.22
raft = 0
raft_surface_layers = 2
raft_surface_thickness = 0.1
raft_surface_line_width = 0.4
raft_surface_line_spacing = 0.4
raft_interface_thickness = 0.15
raft_interface_line_width = 0.7
raft_interface_line_spacing = 0.9
raft_base_thickness = 0.3
raft_base_line_width = 0.8
raft_base_line_spacing = 1.6
raft_surface_speed = 20
raft_interface_speed = 15
raft_base_speed = 15
raft_surface_acceleration = 3000
raft_interface_acceleration = 3000
raft_base_acceleration = 3000
raft_surface_jerk = 20
raft_interface_jerk = 20
raft_base_jerk = 20
raft_surface_fan_speed = 0
raft_interface_fan_speed = 0
raft_base_fan_speed = 0
prime_tower_enable = false
prime_tower_size = 15
prime_tower_wall_thickness = 2
prime_tower_position_x = 200
prime_tower_position_y = 200
prime_tower_flow = 100
prime_tower_wipe_enabled = true
dual_pre_wipe = true
ooze_shield_enabled = false
ooze_shield_angle = 60
ooze_shield_dist = 2
meshfix_union_all = true
meshfix_union_all_remove_holes = false
meshfix_extensive_stitching = false
meshfix_keep_open_polygons = false
multiple_mesh_overlap = 0.15
carve_multiple_volumes = true
alternate_carve_order = true
print_sequence = all_at_once
infill_mesh = false
infill_mesh_order = 0
support_mesh = false
anti_overhang_mesh = false
magic_mesh_surface_mode = normal
magic_spiralize = false
draft_shield_enabled = false
draft_shield_dist = 10
draft_shield_height_limitation = full
draft_shield_height = 10
conical_overhang_enabled = false
conical_overhang_angle = 50
coasting_enable = false
coasting_volume = 0.064
coasting_min_volume = 0.8
coasting_speed = 90
skin_outline_count = 0
skin_alternate_rotation = false
support_conical_enabled = false
support_conical_angle = 30
support_conical_min_width = 5
infill_hollow = false
magic_fuzzy_skin_enabled = false
magic_fuzzy_skin_thickness = 0.3
magic_fuzzy_skin_point_dist = 0.8
wireframe_enabled = false
wireframe_height = 3
wireframe_roof_inset = 3
wireframe_printspeed_bottom = 5
wireframe_printspeed_up = 5
wireframe_printspeed_down = 5
wireframe_printspeed_flat = 5
wireframe_flow_connection = 100
wireframe_flow_flat = 100
wireframe_top_delay = 0
wireframe_bottom_delay = 0
wireframe_flat_delay = 0.1
wireframe_up_half_speed = 0.3
wireframe_top_jump = 0.6
wireframe_fall_down = 0.5
wireframe_drag_along = 0.6
wireframe_strategy = compensate
wireframe_straight_before_down = 20
wireframe_roof_fall_down = 2
wireframe_roof_drag_along = 0.8
wireframe_roof_outer_delay = 0.2
wireframe_nozzle_clearance = 1
temperature = 200
z_offset = 0
cut_bottom = 0
detect_filament_runout = 1
detect_head_shake = 1
detect_head_tilt = 1
flux_calibration = 1
pause_at_layers ="""

ini_constraint = {
    'avoid_crossing_perimeters': [binary],
    'bed_shape': [ignore],
    'bed_temperature': [ignore],
    'before_layer_gcode': [free],
    'bottom_solid_layers': [int_range, 0, 20],
    'bridge_acceleration': [binary],
    'bridge_fan_speed': [percentage],
    'bridge_flow_ratio': False,
    'bridge_speed': [int_range, 1, 150],
    'brim_width': [int_range, 0, 99],
    'complete_objects': False,
    'cooling': [binary],
    'default_acceleration': False,
    'disable_fan_first_layers': [int_range, 0],
    'dont_support_bridges': [binary],
    'duplicate_distance': False,
    'end_gcode': [free],
    'external_fill_pattern': [finite_choice, ['rectilinear-grid', 'line', 'rectilinear', 'honeycomb', 'AUTOMATIC', 'GRID', 'LINES', 'CONCENTRIC']],
    'external_perimeter_extrusion_width': False,
    'external_perimeter_speed': [float_or_percent],
    'external_perimeters_first': False,
    'extra_perimeters': [binary],
    'extruder_clearance_height': False,
    'extruder_clearance_radius': False,
    'extruder_offset': [ignore],
    'extrusion_axis': False,
    'extrusion_multiplier': False,
    'extrusion_width': False,
    'fan_always_on': [binary],
    'fan_below_layer_time': [int_range, 0],
    'filament_colour': [ignore],
    'filament_diameter': False,
    'fill_angle': False,
    'fill_density': [percentage],
    'fill_pattern': [finite_choice, ['rectilinear-grid', 'line', 'rectilinear', 'honeycomb', 'AUTOMATIC', 'GRID', 'LINES', 'CONCENTRIC']],
    'first_layer_acceleration': [binary],
    'first_layer_bed_temperature': [ignore],
    'first_layer_extrusion_width': [percentage, 0, 1666],
    'first_layer_height': [float_range, 0.02, 0.4],
    'first_layer_speed': [int_range, 1, 150],
    'first_layer_temperature': [int_range, 10, 230],
    'gap_fill_speed': [int_range, 1, 150],
    'gcode_arcs': False,
    'gcode_comments': [ignore],
    'gcode_flavor': [free],
    'infill_acceleration': [binary],
    'infill_every_layers': [int_range, 0],
    'infill_extruder': False,
    'infill_extrusion_width': False,
    'infill_first': False,
    'infill_only_where_needed': False,
    'infill_overlap': [percentage],
    'infill_speed': [int_range, 1, 150],
    'interface_shells': False,
    'layer_gcode': False,
    'layer_height': [float_range, 0.02, 0.4],
    'max_fan_speed': [percentage],
    'max_print_speed': False,
    'max_volumetric_speed': False,
    'min_fan_speed': [int_range, 0, 100],
    'min_print_speed': False,
    'min_skirt_length': False,
    'notes': False,
    'nozzle_diameter': [float_range],
    'octoprint_apikey': [ignore],
    'octoprint_host': [ignore],
    'only_retract_when_crossing_perimeters': [binary],
    'ooze_prevention': [binary],
    'output_filename_format': [free],
    'overhangs': [binary],
    'perimeter_acceleration': False,
    'perimeter_extruder': False,
    'perimeter_extrusion_width': False,
    'perimeter_speed': [int_range, 1, 150],
    'perimeters': [int_range, 0, 20],
    'post_process': False,
    'pressure_advance': False,
    'raft': [binary],
    'raft_layers': [int_range, 0, 20],
    'resolution': False,
    'retract_before_travel': False,
    'retract_layer_change': False,
    'retract_length': False,
    'retract_length_toolchange': False,
    'retract_lift': False,
    'retract_restart_extra': False,
    'retract_restart_extra_toolchange': False,
    'retract_speed': False,
    'seam_position': False,
    'skirt_distance': [float_range, 0],
    'skirt_height': [int_range, 0],
    'skirts': [int_range, 0, 20],
    'slowdown_below_layer_time': [int_range, 0],
    'small_perimeter_speed': False,
    'solid_infill_below_area': False,
    'solid_infill_every_layers': [int_range, 0],
    'solid_infill_extruder': False,
    'solid_infill_extrusion_width': False,
    'solid_infill_speed': [int_range, 1, 150],
    'spiral_vase': [binary],
    'standby_temperature_delta': [int_range, -400, 400],
    'start_gcode': False,
    'support_everywhere': [binary],
    'support_material': [binary],
    'support_material_angle': False,
    'support_material_contact_distance': [float_range, 0.0, 10],
    'support_material_enforce_layers': False,
    'support_material_extruder': False,
    'support_material_extrusion_width': False,
    'support_material_interface_extruder': False,
    'support_material_interface_layers': False,
    'support_material_interface_spacing': False,
    'support_material_interface_speed': [percentage],
    'support_material_pattern': [finite_choice, ['rectilinear-grid', 'line', 'rectilinear', 'honeycomb', 'GRID', 'LINES']],
    'support_material_spacing': False,
    'support_material_speed': [int_range, 1, 150],
    'support_material_threshold': [int_range, 0, 90],
    'temperature': [int_range, 10, 230],
    'thin_walls': [binary],
    'threads': False,
    'toolchange_gcode': False,
    'top_infill_extrusion_width': False,
    'top_solid_infill_speed': [int_range, 1, 150],
    'top_solid_layers': [int_range, 0, 20],
    'travel_speed': [int_range, 1, 200],
    'use_firmware_retraction': [binary],
    'use_relative_e_distances': [binary],
    'use_volumetric_e': [binary],
    'vibration_limit': [free],
    'wipe': False,
    'xy_size_compensation': False,
    'z_offset': [float_range, -10, 190],
    'flux_refill_empty': [binary],
    'flux_first_layer': [binary],
    'flux_raft': [binary],
    'cut_bottom': [float_range, -1, 240],
    'detect_filament_runout': [binary],
    'detect_head_shake': [binary],
    'detect_head_tilt': [binary],
    'flux_calibration': [binary],
    'pause_at_layers': False,
    'cura2': [binary],
    'fake_print': [int_range, 0, 9999],
    'geometric_error_correction_on': [binary]
}

ini_flux_params = ['cut_bottom' ,'flux_', 'detect_', 'pause_at_layers', 'geometric_error_correction_on', 'cura2', 'z_offset', 'detect_filament_runout', 'detect_head_shake', 'flux_calibration']