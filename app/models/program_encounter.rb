class ProgramEncounter < ActiveRecord::Base
  set_table_name :program_encounter
  set_primary_key :program_encounter_id
  include Openmrs

end