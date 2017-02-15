## ./stonehearth/ - events
*I can't promise that these are all events.*

Arguments are read as follows -> `<name>: <type>`. While the type is just the variable which was assigned to the name.

Object | Name | Arguments | Async | file
------ | ---- | --------- | ----- | ----
entity | ``stonehearth:admiring_fire``  |  | ✔ | stonehearth\ai\actions\admire_fire_adjacent_action.lua
entity | ``stonehearth:tame_animal``  | animal: animal | ✔ | stonehearth\ai\actions\claim_animal_for_pasture.lua
entity | ``stonehearth:eat_food``  | consumer: entity, time: stonehearth.calendar:get_time_and_date(), food_uri: food:get_uri(), food_data: self._food_data, food_name: food_name, food_quality: self:_get_quality(food) | ✔ | stonehearth\ai\actions\eat_item_action.lua
stonehearth.personality | ``stonehearth:journal_event``  | entity: entity, description: self._food_data.journal_message | ✔ | stonehearth\ai\actions\eat_item_action.lua
entity | ``stonehearth:feed_pasture``  | pasture: pasture | ✔ | stonehearth\ai\actions\feed_pasture_adjacent_action.lua
entity | ``stonehearth:harvest_crop``  | crop_uri: self._crop:get_uri() | ✖ | stonehearth\ai\actions\harvest_crop_adjacent.lua
entity | ``stonehearth:gather_renewable_resource``  | harvested_target: resource, spawned_item: spawned_item | ✔ | stonehearth\ai\actions\harvest_renewable_resource_adjacent.lua
stonehearth.personality | ``stonehearth:journal_event``  | entity: entity, description: description | ✔ | stonehearth\ai\actions\harvest_resource_node_adjacent.lua
entity | ``stonehearth:leave_animal_in_pasture``  | animal: args.animal | ✔ | stonehearth\ai\actions\leave_animal_in_pasture_action.lua
entity | ``stonehearth:town_protection_completed``  | id: entity:get_id(), duration: patrol_duration | ✔ | stonehearth\ai\actions\log_patrol_time_action.lua
ghost | ``stonehearth:item_placed_on_structure``  | ghost_id: ghost:get_id(), placed_item: self._root_entity, structure: options.structure | ✖ | stonehearth\ai\actions\place_carrying_on_structure_adjacent_action.lua
entity | ``stonehearth:repaired_entity``  |  | ✔ | stonehearth\ai\actions\repair_entity_adjacent_action.lua
healer | ``stonehearth:healer:healed_entity_in_combat``  | entity: target | ✔ | stonehearth\ai\actions\combat\execute_heal_action.lua
args.target | ``stonehearth:combat:hit_stun``  | stun_always: args.stun_always | ✔ | stonehearth\ai\actions\combat\trigger_hit_stun_action.lua
entity | ``stonehearth:start_conversation``  | entity: target, conversation_effects: conversation_effects, leader: Boolean | ✔ | stonehearth\ai\actions\conversation\trigger_conversation_action.lua
target | ``stonehearth:start_conversation``  | entity: entity, conversation_effects: follower_conversation_effects | ✔ | stonehearth\ai\actions\conversation\trigger_conversation_action.lua
entity | ``stonehearth:repaired_entity``  | entity: injured_entity | ✔ | stonehearth\ai\actions\health\heal_entity_adjacent_action.lua
injured_entity | ``stonehearth:entity:healed``  | healer: entity | ✔ | stonehearth\ai\actions\health\heal_entity_adjacent_action.lua
entity | ``stonehearth:mined_location``  | location: block | ✖ | stonehearth\ai\actions\mining\dig_adjacent_action.lua
args.citizen | ``stonehearth:incapacitation:dropping``  | None | ✖ | stonehearth\ai\actions\rescue\drop_carried_citizen_action.lua
entity | ``stonehearth:sleep_in_bed``  | bed: bed, is_owner: args.is_owner | ✔ | stonehearth\ai\actions\sleeping\sleep_in_bed_adjacent_action.lua
entity | ``stonehearth:finished_sleeping``  | bed: bed, is_owner: args.is_owner | ✔ | stonehearth\ai\actions\sleeping\sleep_in_bed_adjacent_action.lua
entity | ``stonehearth:sleep_on_ground``  | None | ✔ | stonehearth\ai\actions\sleeping\sleep_on_ground_action.lua
entity | ``stonehearth:finished_sleeping``  | None | ✔ | stonehearth\ai\actions\sleeping\sleep_on_ground_action.lua
entity | ``stonehearth:clear_trap``  | trapped_entity_id: trapped_entity_id | ✔ | stonehearth\ai\actions\trapping\check_bait_trap_adjacent_action.lua
self._entity | ``stonehearth:befriend_pet``  | pet_id: pet_id | ✔ | stonehearth\ai\actions\trapping\check_bait_trap_adjacent_action.lua
entity | ``stonehearth:town_protection_completed``  | id: entity:get_id(), duration: duration | ✔ | stonehearth\ai\actions\unit_control\unit_wait_at_location_action.lua
self._sv._entity | ``stonehearth:malnourished_animal_event``  | None | ✔ | stonehearth\ai\observers\animal_calorie_observer.lua
self._entity | ``stonehearth:malnourishment_event``  | None | ✔ | stonehearth\ai\observers\calorie_observer.lua
item | ``stonehearth:item_undeployed``  | None | ✔ | stonehearth\call_handlers\place_item_call_handler.lua
self._entity | ``stonehearth:ai:halt``  | None | ✖ | stonehearth\components\ai\ai_component.lua
self._entity | ``stonehearth:attribute_changed:`` + <name> | name: name, entity: self._entity | ✔ | stonehearth\components\attributes\attributes_component.lua
self._entity | ``stonehearth:construction:active_changed``  | None | ✖ | stonehearth\components\building\building_component.lua
self._entity | ``stonehearth:construction:active_changed``  | None | ✖ | stonehearth\components\building\building_component.lua
entity | ``stonehearth:construction:dependencies_finished_changed``  | None | ✖ | stonehearth\components\building\building_component.lua
self._entity | ``stonehearth:carry_block:carrying_changed``  | None | ✔ | stonehearth\components\carry_block\carry_block_component.lua
self._entity | ``stonehearth:carry_block:carrying_changed``  | None | ✔ | stonehearth\components\carry_block\carry_block_component.lua
self._entity | ``stonehearth:combat:in_combat_changed``  | in_combat: curr_in_combat | ✖ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat:assaulting_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat:primary_target_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat:stance_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat:panic_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat_state:leash_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat_state:leash_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat_state:leash_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:combat_state:leash_changed``  | None | ✔ | stonehearth\components\combat_state\combat_state_component.lua
self._entity | ``stonehearth:construction:finished_changed``  | entity: self._entity | ✔ | stonehearth\components\construction_progress\construction_progress_component.lua
self._entity | ``stonehearth:construction:teardown_changed``  | entity: self._entity | ✔ | stonehearth\components\construction_progress\construction_progress_component.lua
self._entity | ``stonehearth:door:lock_changed``  | None | ✖ | stonehearth\components\door\door_component.lua
self._entity | ``stonehearth:on_removed_from_world``  | None | ✖ | stonehearth\components\entity_forms\entity_forms_component.lua
self._entity | ``stonehearth:on_added_to_world``  | None | ✖ | stonehearth\components\entity_forms\entity_forms_component.lua
self._entity | ``stonehearth:equipment_changed``  | None | ✔ | stonehearth\components\equipment\equipment_component.lua
self._entity | ``stonehearth:equipment_piece:equip_changed``  | None | ✖ | stonehearth\components\equipment_piece\equipment_piece_component.lua
self._entity | ``stonehearth:equipment_piece:equip_changed``  | None | ✖ | stonehearth\components\equipment_piece\equipment_piece_component.lua
self._entity | ``stonehearth:on_evolved``  | entity: self._entity, evolved_form: evolved_form | ✖ | stonehearth\components\evolve\evolve_component.lua
self._entity | ``stonehearth:expendable_resource_changed:`` + <resource_name> | name: resource_name, entity: self._entity | ✔ | stonehearth\components\expendable_resources\expendable_resources_component.lua
building | ``stonehearth:construction:scaffolding_project_complete``  | None | ✖ | stonehearth\components\fabricator\fabricator_component.lua
stonehearth | ``stonehearth:fire:lit``  | lit: Boolean, player_id: radiant.entities.get_player_id(self._entity), entity: self._entity | ✔ | stonehearth\components\firepit\firepit_component.lua
self._entity | ``stonehearth:happiness:thought_added``  | thought: thought_key | ✔ | stonehearth\components\happiness\happiness_component.lua
self._entity | ``stonehearth:mood_changed``  | None | ✔ | stonehearth\components\happiness\happiness_component.lua
self._entity | ``stonehearth:incapacitation:was_picked_up``  | None | ✖ | stonehearth\components\incapacitation\incapacitation_component.lua
self._entity | ``stonehearth:incapacitation:was_dropped``  | None | ✖ | stonehearth\components\incapacitation\incapacitation_component.lua
entity | ``stonehearth:entity:became_incapacitated``  | None | ✖ | stonehearth\components\incapacitation\incapacitation_component.lua
entity | ``stonehearth:entity:incapacitate_state_changed``  | None | ✔ | stonehearth\components\incapacitation\incapacitation_component.lua
entity | ``stonehearth:entity:incapacitate_state_changed``  | None | ✔ | stonehearth\components\incapacitation\incapacitation_component.lua
entity | ``stonehearth:entity:incapacitate_state_changed``  | None | ✔ | stonehearth\components\incapacitation\incapacitation_component.lua
stonehearth.personality | ``stonehearth:journal_event``  | entity: self._entity, description: activity_name | ✔ | stonehearth\components\job\job_component.lua
self._entity | ``stonehearth:job_changed``  | entity: self._entity | ✖ | stonehearth\components\job\job_component.lua
self._entity | ``stonehearth:level_up``  | level: new_level, job_uri: self._sv.job_uri, job_name: self._sv.curr_job_name | ✔ | stonehearth\components\job\job_component.lua
self._entity | ``stonehearth:lease_released``  | lease_name: lease_name | ✔ | stonehearth\components\lease\lease_component.lua
self._entity | ``stonehearth:mining:enable_changed``  | None | ✔ | stonehearth\components\mining_zone\mining_zone_component.lua
self._entity | ``stonehearth:mount:owner_changed``  | None | ✔ | stonehearth\components\mount\mount_component.lua
self._entity | ``stonehearth:mount:owner_changed``  | None | ✔ | stonehearth\components\mount\mount_component.lua
self._entity | ``stonehearth:owner_changed``  | new_owner: self._sv.owner | ✔ | stonehearth\components\ownership\ownable_object_component.lua
self._entity | ``stonehearth:party:size_changed``  | size: self._sv.party_size | ✔ | stonehearth\components\party\party_component.lua
self._entity | ``stonehearth:party:size_changed``  | size: self._sv.party_size | ✔ | stonehearth\components\party\party_component.lua
self._entity | ``stonehearth:party:party_changed``  | None | ✔ | stonehearth\components\party_member\party_member_component.lua
self._entity | ``stonehearth:posture_changed``  | None | ✔ | stonehearth\components\posture\posture_component.lua
self._entity | ``stonehearth:posture_changed``  | None | ✔ | stonehearth\components\posture\posture_component.lua
self._entity | ``stonehearth:combat:projectile_impact``  | None | ✔ | stonehearth\components\projectile\projectile_component.lua
self._entity | ``stonehearth:on_renewable_resource_renewed``  | target: self._entity, available_resource: self._resource | ✖ | stonehearth\components\renewable_resource_node\renewable_resource_node_component.lua
self._entity | ``stonehearth:renewable_resource_spawned``  | target: self._entity, item: item | ✖ | stonehearth\components\renewable_resource_node\renewable_resource_node_component.lua
self._entity | ``stonehearth:on_renewable_resource_renewed``  | target: self._entity, available_resource: json.resource | ✖ | stonehearth\components\renewable_resource_node\renewable_resource_node_component.lua
owner | ``stonehearth:gather_resource``  | harvested_target: self._entity, spawned_item: item | ✖ | stonehearth\components\resource_node\resource_node_component.lua
self | ``stonehearth:construction:scaffolding_project_complete``  | None | ✖ | stonehearth\components\scaffolding\scaffolding_project.lua
self | ``stonehearth:construction:scaffolding_project_complete``  | None | ✖ | stonehearth\components\scaffolding\scaffolding_project_flat.lua
self | ``stonehearth:construction:scaffolding_project_complete``  | None | ✖ | stonehearth\components\scaffolding\scaffolding_project_flat.lua
self | ``stonehearth:construction:scaffolding_project_complete``  | None | ✖ | stonehearth\components\scaffolding\scaffolding_project_volume.lua
self | ``stonehearth:construction:scaffolding_project_complete``  | None | ✖ | stonehearth\components\scaffolding\scaffolding_project_volume.lua
self._sv.animal | ``stonehearth:shepherded_animal_follow_status_change``  | should_follow: self._sv.should_follow, shepherd: shepherd | ✖ | stonehearth\components\shepherd_pasture\shepherded_animal_component.lua
self._entity | ``stonehearth:on_pasture_animals_changed``  |  | ✖ | stonehearth\components\shepherd_pasture\shepherd_pasture_component.lua
self._entity | ``stonehearth:on_pasture_animals_changed``  |  | ✖ | stonehearth\components\shepherd_pasture\shepherd_pasture_component.lua
self._entity | ``stonehearth:siege_weapon:needs_refill``  | None | ✖ | stonehearth\components\siege_weapon\siege_weapon_component.lua
self._entity | ``stonehearth:siege_weapon:ammo_status_changed``  | out_of_ammo: Boolean | ✖ | stonehearth\components\siege_weapon\siege_weapon_component.lua
self._entity | ``stonehearth:ending_interaction``  | target: requester | ✔ | stonehearth\components\social\social_component.lua
self | ``stonehearth:interaction:both_ready``  | None | ✔ | stonehearth\components\social\social_component.lua
radiant | ``radiant:item:stacks_changed``  | entity: self._entity | ✖ | stonehearth\components\stacks\stacks_component.lua
self._entity | ``stonehearth:stockpile:item_added``  | stockpile: self._entity, item: item | ✔ | stonehearth\components\stockpile\stockpile_component.lua
self._entity | ``stonehearth:stockpile:item_removed``  | stockpile: self._entity, item: item | ✔ | stonehearth\components\stockpile\stockpile_component.lua
self._inventory | ``stonehearth:inventory:filter_changed``  | None | ✔ | stonehearth\components\storage\storage_component.lua
entity | ``stonehearth:trapped``  | None | ✔ | stonehearth\components\trapping\bait_trap_component.lua
self | ``stonehearth:order_list_changed``  | None | ✖ | stonehearth\components\workshop\craft_order_list.lua
self._entity | ``stonehearth:work_order:status_changed``  | work_order_name: work_order_name, new_status: status | ✔ | stonehearth\components\work_order\work_order_component.lua
stonehearth | ``stonehearth:combat:nonthreatening_changed``  | entity: entity | ✔ | stonehearth\data\buffs\hidden\nonthreatening\nonthreatening_buff.lua
stonehearth | ``stonehearth:combat:nonthreatening_changed``  | entity: entity | ✔ | stonehearth\data\buffs\hidden\nonthreatening\nonthreatening_buff.lua
boss | ``stonehearth:chieftain_camp_moving_on``  | None | ✖ | stonehearth\data\gm\campaigns\goblin_war\arcs\trigger\raidcamp\encounters\goblin_camp_departs.lua
self._sv._entity | ``stonehearth:add_trailing_animal``  | animal: animal, pasture: pasture | ✖ | stonehearth\jobs\shepherd\shepherd.lua
self | ``stonehearth:building_selection_changed``  | None | ✖ | stonehearth\services\client\build_editor\build_editor_service.lua
self | ``stonehearth:sub_selection_changed``  | old_selection: old_selected, new_selection: selected, building: building_entity | ✖ | stonehearth\services\client\build_editor\build_editor_service.lua
entity | ``stonehearth:hilighted_changed``  | None | ✖ | stonehearth\services\client\hilight\hilight_service.lua
radiant | ``stonehearth:ui_mode_changed``  | None | ✔ | stonehearth\services\client\renderer\renderer_service.lua
radiant | ``stonehearth:building_vision_mode_changed``  | None | ✔ | stonehearth\services\client\renderer\renderer_service.lua
last_selected | ``stonehearth:selection_changed``  | None | ✖ | stonehearth\services\client\selection\selection_service.lua
entity | ``stonehearth:selection_changed``  | None | ✖ | stonehearth\services\client\selection\selection_service.lua
radiant | ``stonehearth:selection_changed``  | None | ✖ | stonehearth\services\client\selection\selection_service.lua
self | ``stonehearth:visible_volume_changed``  | None | ✔ | stonehearth\services\client\subterranean_view\subterranean_view_service.lua
stonehearth.bulletin_board | ``stonehearth:trigger_bulletin_for_test``  | bulletin: bulletin, time: stonehearth.calendar:get_time_and_date() | ✔ | stonehearth\services\server\bulletin_board\bulletin_board_service.lua
party | ``stonehearth:combat:target_acquired``  | attacker: entity, target: target | ✔ | stonehearth\services\server\combat\combat_service.lua
population | ``stonehearth:population:engaged_in_combat``  | entity: target, entity_id: target:get_id() | ✔ | stonehearth\services\server\combat\combat_service.lua
data.party | ``stonehearth:party_unit_command_completed``  | None | ✔ | stonehearth\services\server\combat_server_commands\combat_server_commands_service.lua
self | ``stonehearth:game_mode_changed``  | None | ✔ | stonehearth\services\server\game_creation\game_creation_service.lua
info.event_to_broadcast | None |  | ✖ | stonehearth\services\server\game_master\controllers\encounters\city_tier_achieved_encounter.lua
ctx.encounter_name | ``stonehearth:create_camp_complete``  |  | ✔ | stonehearth\services\server\game_master\controllers\encounters\create_camp_encounter.lua
self | ``stonehearth:dynamic_scenario:finished``  | None | ✖ | stonehearth\services\server\game_master\controllers\script_encounters\returning_trader_script.lua
self | ``stonehearth:dynamic_scenario:finished``  | None | ✖ | stonehearth\services\server\game_master\controllers\script_encounters\returning_trader_script.lua
self | ``stonehearth:dynamic_scenario:finished``  | None | ✖ | stonehearth\services\server\game_master\controllers\script_encounters\simple_caravan_script.lua
self | ``stonehearth:dynamic_scenario:finished``  | None | ✖ | stonehearth\services\server\game_master\controllers\script_encounters\simple_caravan_script.lua
self | ``stonehearth:hydrology:water_bodies_merged``  | None | ✔ | stonehearth\services\server\hydrology\hydrology_service.lua
self | ``stonehearth:inventory:storage_added``  | storage: storage | ✖ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:storage_removed``  | storage_id: id | ✖ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:public_storage_full_changed``  | None | ✔ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:stockpile_added``  | stockpile: stockpile | ✖ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:stockpile_removed``  | stockpile: stockpile | ✖ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:item_updated``  | item: item | ✖ | stonehearth\services\server\inventory\inventory.lua
radiant | ``stonehearth:inventory:container_changed``  | entity: item | ✔ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:item_added``  | item: item | ✖ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:item_removed``  | item_id: item_id | ✖ | stonehearth\services\server\inventory\inventory.lua
radiant | ``stonehearth:inventory:container_changed``  | entity: item | ✔ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory:fullness_changed``  | None | ✔ | stonehearth\services\server\inventory\inventory.lua
self | ``stonehearth:inventory_tracker:item_added:sync``  | key: key, item: entity | ✖ | stonehearth\services\server\inventory\inventory_tracker.lua
self | ``stonehearth:inventory_tracker:item_added``  | key: key | ✔ | stonehearth\services\server\inventory\inventory_tracker.lua
self | ``stonehearth:inventory_tracker:item_removed:sync``  | key: key, item_id: entity_id | ✖ | stonehearth\services\server\inventory\inventory_tracker.lua
self | ``stonehearth:inventory_tracker:item_removed``  | key: key | ✔ | stonehearth\services\server\inventory\inventory_tracker.lua
get_jobs_controller(player_id) | ``stonehearth:job:job_presence_changed``  | is_combat_job: self:is_combat_job() | ✔ | stonehearth\services\server\job\job_info_controller.lua
get_jobs_controller(player_id) | ``stonehearth:job:job_presence_changed``  | is_combat_job: self:is_combat_job() | ✔ | stonehearth\services\server\job\job_info_controller.lua
_radiant | ``radiant:player_kingdom_changed``  | player_id: player_id | ✖ | stonehearth\services\server\player\player_service.lua
pop | ``stonehearth:amenity_changed``  | other_player: player_b | ✔ | stonehearth\services\server\player\player_service.lua
pop | ``stonehearth:amenity_changed``  | other_player: player_a | ✔ | stonehearth\services\server\player\player_service.lua
radiant | ``stonehearth:amenity:sync_changed``  | faction_a: player_a, faction_b: player_b | ✖ | stonehearth\services\server\player\player_service.lua
pop | ``stonehearth:amenity_changed``  | None | ✔ | stonehearth\services\server\player\player_service.lua
stonehearth.population | ``stonehearth:population:entity_destroyed``  | entity_id: entity_id | ✔ | stonehearth\services\server\population\population_faction.lua
stonehearth | ``stonehearth:population:work_order_suspended``  | work_order_name: work_order, is_suspended: is_suspended, player_id: self._sv.player_id | ✔ | stonehearth\services\server\population\population_faction.lua
entity | ``stonehearth:entity:toggle_rescue``  | None | ✔ | stonehearth\services\server\population\population_service.lua
self | ``stonehearth:item_bought``  | item_uri: uri, item_cost: item_cost, quantity: buy_quantity | ✔ | stonehearth\services\server\shop\shop.lua
self | ``stonehearth:town:medic_available``  | None | ✖ | stonehearth\services\server\town\town.lua
requester | ``stonehearth:town:medic_unavailable``  | None | ✖ | stonehearth\services\server\town\town.lua
self | ``stonehearth:town:medic_available``  | None | ✖ | stonehearth\services\server\town\town.lua
self | ``stonehearth:patrol_route_available``  | player_id: player_id | ✔ | stonehearth\services\server\town_patrol\town_patrol_service.lua
###### A total of **158** events found while parsing **796** files.
