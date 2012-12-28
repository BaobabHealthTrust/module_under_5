class ProgramEncounterDetails < ActiveRecord::Base
  set_table_name :program_encounter_details
  set_primary_key :id
  include Openmrs

end