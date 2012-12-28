
class ClinicController < ApplicationController

  def index

    redirect_to "/patients/show/#{params[:ext_patient_id]}?user_id=#{params[:user_id]}" if !params[:ext_patient_id].nil?

    @project = get_global_property_value("project.name") rescue "Unknown"

    @facility = get_global_property_value("facility.name") rescue "Unknown"

    @patient_registration = get_global_property_value("patient.registation.url") rescue ""

  end

  def user_login

    link = get_global_property_value("user.management.url").to_s rescue nil

    if link.nil?
      flash[:error] = "Missing configuration for <br/>user management connection!"

      redirect_to "/no_user" and return
    end

    host = request.host_with_port rescue ""

    redirect_to "#{link}/login?ext=true&src=#{host}" and return if params[:ext_user_id].nil?

  end

  def user_logout

    link = get_global_property_value("user.management.url").to_s rescue nil


    if link.nil?
      flash[:error] = "Missing configuration for <br/>user management connection!"

      redirect_to "/no_user" and return
    end

    host = request.host_with_port rescue ""

    redirect_to "#{link}/logout/#{params[:id]}?ext=true&src=#{host}" and return if params[:ext_user_id].nil?

  end

end