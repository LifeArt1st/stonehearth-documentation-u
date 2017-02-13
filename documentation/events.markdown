##### stonehearth\ai\actions\admire_fire_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:admiring_fire |  {} | Empty | ✔
##### stonehearth\ai\actions\claim_animal_for_pasture.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:tame_animal |  {animal = animal} | Empty | ✔
##### stonehearth\ai\actions\eat_item_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:eat_food | consumer, time | Empty | ✔
stonehearth:journal_event | entity, description | Empty | ✔
##### stonehearth\ai\actions\feed_pasture_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:feed_pasture |  {pasture = pasture} | Empty | ✔
##### stonehearth\ai\actions\harvest_crop_adjacent.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:harvest_crop |  {crop_uri = self._crop:get_uri( | Empty | ✖
##### stonehearth\ai\actions\harvest_renewable_resource_adjacent.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:journal_event | entity, description, substitutions | Empty | ✔
stonehearth:gather_renewable_resource | harvested_target, spawned_item | Empty | ✔
##### stonehearth\ai\actions\harvest_resource_node_adjacent.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:journal_event | entity, description | Empty | ✔
##### stonehearth\ai\actions\leave_animal_in_pasture_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:leave_animal_in_pasture |  {animal = args.animal} | Empty | ✔
##### stonehearth\ai\actions\log_patrol_time_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:town_protection_completed |  {
         id = entity:get_id( | Empty | ✔
##### stonehearth\ai\actions\place_carrying_on_structure_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:item_placed_on_structure |  {ghost_id = ghost:get_id( | Empty | ✖
##### stonehearth\ai\actions\produce_crafted_items.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:crafter:craft_item |  crafting_data | Empty | ✔
##### stonehearth\ai\actions\repair_entity_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:repaired_entity |  { action = 'refill_ammo' } | Empty | ✔
stonehearth:repaired_entity |  {} | Empty | ✔
##### stonehearth\ai\actions\trigger_event.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
rgs.event_nam |  args.event_args | Empty | ✔
rgs.event_nam |  args.event_args | Empty | ✖
##### stonehearth\ai\actions\combat\execute_heal_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:healer:healed_entity_in_combat |  { entity = target } | Empty | ✔
##### stonehearth\ai\actions\combat\trigger_hit_stun_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:combat:hit_stun |  { stun_always = args.stun_always } | Empty | ✔
##### stonehearth\ai\actions\conversation\trigger_conversation_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:start_conversation | entity, conversation_effects | Empty | ✔
stonehearth:start_conversation | entity, conversation_effects, leader | Empty | ✔
##### stonehearth\ai\actions\health\heal_entity_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:entity:healed |  { healer = entity } | Empty | ✔
stonehearth:repaired_entity |  { entity = injured_entity } | Empty | ✔
##### stonehearth\ai\actions\mining\dig_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:mined_location |  { location = block } | Empty | ✖
##### stonehearth\ai\actions\rescue\drop_carried_citizen_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:incapacitation:dropping | None | Empty | ✖
##### stonehearth\ai\actions\sleeping\sleep_in_bed_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:sleep_in_bed | bed, is_owner | Empty | ✔
stonehearth:finished_sleeping | bed, is_owner | Empty | ✔
##### stonehearth\ai\actions\sleeping\sleep_on_ground_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:sleep_on_ground | None | Empty | ✔
stonehearth:finished_sleeping | None | Empty | ✔
##### stonehearth\ai\actions\trapping\check_bait_trap_adjacent_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:clear_trap |  {trapped_entity_id = trapped_entity_id} | Empty | ✔
stonehearth:befriend_pet |  {pet_id = pet_id} | Empty | ✔
##### stonehearth\ai\actions\unit_control\unit_wait_at_location_action.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:town_protection_completed |  {
         id = entity:get_id( | Empty | ✔
##### stonehearth\ai\observers\animal_calorie_observer.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:malnourished_animal_event | None | Empty | ✔
##### stonehearth\ai\observers\calorie_observer.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:malnourishment_event | None | Empty | ✔
##### stonehearth\ai\observers\ogos_mountain_observer.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:goblin_campaign:mountain_listens |  nil | Empty | ✔
##### stonehearth\call_handlers\place_item_call_handler.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:item_undeployed | None | Empty | ✔
##### stonehearth\components\ai\ai_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:ai:halt | None | Empty | ✖
##### stonehearth\components\attributes\attributes_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:attribute_changed:' .. nam | name, entity | Empty | ✔
##### stonehearth\components\buffs\buffs_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:buff_added | entity, uri, buff | Empty | ✔
stonehearth:buff_removed | entity, uri, buff | Empty | ✔
##### stonehearth\components\building\building_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:active_changed | None | Empty | ✖
stonehearth:construction:dependencies_finished_changed | None | Empty | ✖
stonehearth:construction:structure_finished_changed |  entry.entity | Empty | ✖
##### stonehearth\components\carry_block\carry_block_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:carry_block:carrying_changed | None | Empty | ✔
##### stonehearth\components\combat_state\combat_state_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:combat:assaulting_changed | None | Empty | ✔
stonehearth:combat:primary_target_changed | None | Empty | ✔
stonehearth:combat:in_combat_changed |  { in_combat = curr_in_combat } | Empty | ✖
stonehearth:combat:stance_changed | None | Empty | ✔
stonehearth:combat_state:leash_changed | None | Empty | ✔
stonehearth:combat:panic_changed | None | Empty | ✔
##### stonehearth\components\construction_progress\construction_progress_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:finished_changed |  { 
         entity = self._entity
      } | Empty | ✔
stonehearth:construction:teardown_changed |  { 
         entity = self._entity
      } | Empty | ✔
##### stonehearth\components\defense_zone\defense_zone_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:combat:leash_contents_changed |  args | Empty | ✔
##### stonehearth\components\door\door_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:door:lock_changed | None | Empty | ✖
##### stonehearth\components\entity_forms\entity_forms_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:on_removed_from_world | None | Empty | ✖
stonehearth:on_added_to_world | None | Empty | ✖
##### stonehearth\components\equipment\equipment_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:equipment_changed | None | Empty | ✔
##### stonehearth\components\equipment_piece\equipment_piece_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:equipment_piece:equip_changed | None | Empty | ✖
##### stonehearth\components\evolve\evolve_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:on_evolved | entity, evolved_form | Empty | ✖
##### stonehearth\components\expendable_resources\expendable_resources_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:expendable_resource_changed:' .. resource_nam | name, entity | Empty | ✔
##### stonehearth\components\fabricator\fabricator_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:waiting_for_anti_dependencies |  self._entity | Empty | ✖
stonehearth:construction:scaffolding_project_complete | None | Empty | ✖
##### stonehearth\components\firepit\firepit_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:fire:lit | lit, player_id | Empty | ✔
stonehearth:fire:lit | lit, entity, player_id | Empty | ✔
##### stonehearth\components\growing\growing_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:growing | entity, stage, finished | Empty | ✔
##### stonehearth\components\happiness\happiness_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:mood_changed | None | Empty | ✔
stonehearth:happiness:thought_added |  { thought = thought_key } | Empty | ✔
##### stonehearth\components\incapacitation\incapacitation_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:incapacitation:was_picked_up | None | Empty | ✖
stonehearth:incapacitation:was_dropped | None | Empty | ✖
stonehearth:entity:became_incapacitated | None | Empty | ✔
stonehearth:entity:incapacitate_state_changed | None | Empty | ✔
##### stonehearth\components\job\job_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:journal_event | entity, description | Empty | ✔
stonehearth:job_changed |  { entity = self._entity } | Empty | ✖
stonehearth:level_up | level, job_uri, job_name | Empty | ✔
##### stonehearth\components\lease\lease_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:lease_released |  { lease_name = lease_name } | Empty | ✔
##### stonehearth\components\mining_zone\mining_zone_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:mining:enable_changed | None | Empty | ✔
##### stonehearth\components\mount\mount_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:mount:owner_changed | None | Empty | ✔
##### stonehearth\components\ownership\ownable_object_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:owner_changed |  {new_owner = self._sv.owner} | Empty | ✔
##### stonehearth\components\party\party_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:party:size_changed |  {size = self._sv.party_size} | Empty | ✔
##### stonehearth\components\party_member\party_member_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:party:party_changed | None | Empty | ✔
##### stonehearth\components\posture\posture_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:posture_changed | None | Empty | ✔
##### stonehearth\components\projectile\projectile_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:combat:projectile_impact | None | Empty | ✔
##### stonehearth\components\renewable_resource_node\renewable_resource_node_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:on_renewable_resource_renewed | target, available_resource | Empty | ✖
stonehearth:renewable_resource_spawned | target, item | Empty | ✖
stonehearth:on_renewable_resource_renewed | target, available_resource | Empty | ✖
##### stonehearth\components\resource_node\resource_node_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:gather_resource | harvested_target, spawned_item | Empty | ✖
##### stonehearth\components\scaffolding\scaffolding_project.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:scaffolding_project_complete | None | Empty | ✖
##### stonehearth\components\scaffolding\scaffolding_project_flat.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:scaffolding_project_complete | None | Empty | ✖
##### stonehearth\components\scaffolding\scaffolding_project_volume.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:scaffolding_project_complete | None | Empty | ✖
##### stonehearth\components\scaffolding\scaffolding_region.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:construction:scaffolding_region_destroy_immediately |  self._sv._id | Empty | ✖
stonehearth:construction:scaffolding_region_destroyed |  self._sv._id | Empty | ✖
##### stonehearth\components\score\score_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:score_changed | key, new_score | Empty | ✔
##### stonehearth\components\shepherd_pasture\shepherded_animal_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:shepherded_animal_follow_status_change | should_follow, shepherd | Empty | ✖
##### stonehearth\components\shepherd_pasture\shepherd_pasture_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:on_pasture_animals_changed |  {} | Empty | ✖
stonehearth:shepherd_pasture:feed_changed |  | Empty | ✔
##### stonehearth\components\siege_weapon\siege_weapon_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:siege_weapon:ammo_status_changed |  { out_of_ammo = self._sv.num_uses <= 0 } | Empty | ✖
stonehearth:siege_weapon:ammo_status_changed |  { out_of_ammo = true } | Empty | ✖
stonehearth:siege_weapon:needs_refill | None | Empty | ✖
##### stonehearth\components\social\social_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:interaction:both_ready | None | Empty | ✔
stonehearth:ending_interaction |  { target = requester } | Empty | ✔
##### stonehearth\components\stacks\stacks_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
radiant:item:stacks_changed |  {entity = self._entity} | Empty | ✖
##### stonehearth\components\stockpile\stockpile_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:stockpile:item_removed | stockpile, item | Empty | ✔
stonehearth:stockpile:item_added | stockpile, item | Empty | ✔
##### stonehearth\components\storage\storage_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:storage:filter_changed |  | Empty | ✔
stonehearth:inventory:filter_changed | None | Empty | ✔
stonehearth:storage:item_added | item, item_id | Empty | ✔
stonehearth:storage:item_removed | item_id, item | Empty | ✔
##### stonehearth\components\target_tables\target_table.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:target_table_changed |  | Empty | ✔
##### stonehearth\components\trapping\bait_trap_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:trapped | None | Empty | ✔
##### stonehearth\components\workshop\craft_order_list.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:order_list_changed | None | Empty | ✖
##### stonehearth\components\work_order\work_order_component.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:work_order:status_changed | work_order_name, new_status | Empty | ✔
##### stonehearth\data\buffs\hidden\nonthreatening\nonthreatening_buff.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:combat:nonthreatening_changed |  { entity=entity } | Empty | ✔
##### stonehearth\data\gm\campaigns\goblin_war\arcs\trigger\raidcamp\encounters\goblin_camp_departs.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:chieftain_camp_moving_on | None | Empty | ✖
##### stonehearth\jobs\shepherd\shepherd.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:add_trailing_animal | animal, pasture | Empty | ✖
##### stonehearth\services\client\build_editor\build_editor_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:sub_selection_changed | old_selection, new_selection, building | Empty | ✖
stonehearth:building_selection_changed | None | Empty | ✖
##### stonehearth\services\client\camera\player_camera_controller.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:camera:update | pan, orbit, zoom | Empty | ✔
stonehearth:camera:update | pan, orbit, zoom | Empty | ✔
stonehearth:camera:update | pan, orbit, zoom | Empty | ✔
##### stonehearth\services\client\hilight\hilight_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:hilighted_changed | None | Empty | ✖
##### stonehearth\services\client\renderer\renderer_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:ui_mode_changed | None | Empty | ✔
stonehearth:building_vision_mode_changed | None | Empty | ✔
##### stonehearth\services\client\selection\selection_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:selection_changed | None | Empty | ✖
stonehearth:selection_changed | None | Empty | ✖
stonehearth:selection_changed | None | Empty | ✖
##### stonehearth\services\client\subterranean_view\subterranean_view_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:visible_volume_changed | None | Empty | ✔
##### stonehearth\services\server\bulletin_board\bulletin_board_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:trigger_bulletin_for_test | bulletin, time | Empty | ✔
##### stonehearth\services\server\combat\combat_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:combat:assault |  context | Empty | ✔
stonehearth:combat:target_healed |  context | Empty | ✔
stonehearth:population:engaged_in_combat | entity, entity_id | Empty | ✔
stonehearth:combat:healed |  context | Empty | ✔
stonehearth:combat:target_hit |  context | Empty | ✔
stonehearth:combat:target_acquired | attacker, target | Empty | ✔
stonehearth:combat:battery |  context | Empty | ✔
stonehearth:combat:hit_stun |  context | Empty | ✔
##### stonehearth\services\server\combat_server_commands\combat_server_commands_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:party_unit_command_completed | None | Empty | ✔
##### stonehearth\services\server\game_creation\game_creation_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:journal_event | entity, description | Empty | ✔
stonehearth:game_mode_changed | None | Empty | ✔
##### stonehearth\services\server\game_master\controllers\encounters\city_tier_achieved_encounter.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
nfo.event_to_broadcas |  {} | Empty | ✖
##### stonehearth\services\server\game_master\controllers\encounters\create_camp_encounter.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:create_camp_complete |  {} | Empty | ✔
##### stonehearth\services\server\game_master\controllers\script_encounters\returning_trader_script.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:dynamic_scenario:finished | None | Empty | ✖
##### stonehearth\services\server\game_master\controllers\script_encounters\simple_caravan_script.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:dynamic_scenario:finished | None | Empty | ✖
##### stonehearth\services\server\hydrology\hydrology_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:hydrology:water_bodies_merged | None | Empty | ✔
##### stonehearth\services\server\inventory\inventory.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:inventory:stockpile_removed |  { stockpile = stockpile } | Empty | ✖
stonehearth:inventory:item_removed |  { item_id = item_id } | Empty | ✖
stonehearth:inventory:item_updated |  { item = item } | Empty | ✖
stonehearth:inventory:public_storage_full_changed | None | Empty | ✔
stonehearth:inventory:container_changed |  {entity=item} | Empty | ✔
stonehearth:inventory:storage_added |  { storage = storage } | Empty | ✖
stonehearth:inventory:item_added |  { item = item } | Empty | ✖
stonehearth:inventory:fullness_changed | None | Empty | ✔
stonehearth:inventory:stockpile_added |  { stockpile = stockpile } | Empty | ✖
stonehearth:inventory:storage_removed |  { storage_id = id } | Empty | ✖
##### stonehearth\services\server\inventory\inventory_tracker.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:inventory_tracker:item_removed |  { key = key } | Empty | ✔
stonehearth:inventory_tracker:item_removed:sync | key, item_id | Empty | ✖
stonehearth:inventory_tracker:item_added:sync | key, item | Empty | ✖
stonehearth:inventory_tracker:item_added |  { key = key } | Empty | ✔
##### stonehearth\services\server\job\job_info_controller.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:job:job_presence_changed |  { is_combat_job = self:is_combat_job( | Empty | ✔
##### stonehearth\services\server\player\player_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:amenity:sync_changed | faction_a, faction_b | Empty | ✖
stonehearth:amenity_changed |  { other_player = player_a } | Empty | ✔
stonehearth:amenity_changed |  { other_player = player_b } | Empty | ✔
stonehearth:amenity_changed | None | Empty | ✔
radiant:player_kingdom_changed |  {player_id = player_id} | Empty | ✖
##### stonehearth\services\server\population\population_faction.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
      "stonehearth:population:entity_destroyed |  
      { entity_id = entity_id } | Empty | ✔
stonehearth:population:new_threat | entity_id, entity | Empty | ✔
stonehearth:population:work_order_suspended | work_order_name, is_suspended, player_id | Empty | ✔
##### stonehearth\services\server\population\population_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:entity:toggle_rescue | None | Empty | ✔
##### stonehearth\services\server\shop\shop.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:item_sold | item_uri, item_cost, quantity | Empty | ✔
stonehearth:item_bought | item_uri, item_cost, quantity | Empty | ✔
##### stonehearth\services\server\tasks\task.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
elf._activity.name .. ':work_available | None | Empty | ✔
elf._stat |  self | Empty | ✔
##### stonehearth\services\server\town\town.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:blueprint_added | town, blueprint | Empty | ✔
stonehearth:town:medic_available | None | Empty | ✖
stonehearth:town:medic_unavailable | None | Empty | ✖
##### stonehearth\services\server\town_patrol\town_patrol_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:patrol_route_available |  { player_id = player_id } | Empty | ✔
##### stonehearth\services\server\world_generation\world_generation_service.lua
Event Name | Arguments | Triggered | Async
---------- | --------- | --------- | -----
stonehearth:generate_world_progress |  {
      progress = progress * 100
   } | Empty | ✖
