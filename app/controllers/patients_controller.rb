
class PatientsController < ApplicationController

  def show
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    if @patient.nil?
      redirect_to "/encounters/no_patient" and return
    end

    if params[:user_id].nil?
      redirect_to "/encounters/no_user" and return
    end

    @user = User.find(params[:user_id]) rescue nil
    
    redirect_to "/encounters/no_user" and return if @user.nil?

    @task = TaskFlow.new(params[:user_id], @patient.id)

    @links = {}

    @task.tasks.each{|task|
      @links[task.titleize] = "/protocol_patients/#{task.gsub(/\s/, "_")}?patient_id=#{@patient.id}&user_id=#{params[:user_id]}"
    }

    @project = get_global_property_value("project.name") rescue "Unknown"

    @demographics_url = get_global_property_value("patient.registation.url") rescue nil

    if !@demographics_url.nil?
      @demographics_url = @demographics_url + "/demographics/#{@patient.id}?user_id=#{@user.id}&ext=true"
    end

    @task.next_task

  end

  def current_visit
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    ProgramEncounter.current_date = (session[:date_time] || Time.now)
    
    @programs = @patient.program_encounters.current.collect{|p|

      [
        p.id,
        p.to_s,
        p.program_encounter_types.collect{|e|
          [
            e.encounter_id, e.encounter.type.name,
            e.encounter.encounter_datetime.strftime("%H:%M"),
            e.encounter.creator
          ]
        },
        p.date_time.strftime("%d-%b-%Y")
      ]
    } if !@patient.nil?

    # raise @programs.inspect

    render :layout => false
  end

  def visit_history
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    @programs = @patient.program_encounters.find(:all, :order => ["date_time DESC"]).collect{|p|

      [
        p.id,
        p.to_s,
        p.program_encounter_types.collect{|e|
          [
            e.encounter_id, e.encounter.type.name,
            e.encounter.encounter_datetime.strftime("%H:%M"),
            e.encounter.creator
          ]
        },
        p.date_time.strftime("%d-%b-%Y")
      ]
    } if !@patient.nil?

    # raise @programs.inspect

    render :layout => false
  end

  def demographics
    @patient = Patient.find(params[:id] || params[:patient_id]) rescue nil

    if @patient.nil?
      redirect_to "/encounters/no_patient" and return
    end

    if params[:user_id].nil?
      redirect_to "/encounters/no_user" and return
    end

    @user = User.find(params[:user_id]) rescue nil

    redirect_to "/encounters/no_user" and return if @user.nil?

  end

end
