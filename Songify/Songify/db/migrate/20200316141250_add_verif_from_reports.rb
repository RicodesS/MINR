class AddVerifFromReports < ActiveRecord::Migration[6.0]
  def change
  	add_column :reports, :verif, :boolean, default:false
  end
end
