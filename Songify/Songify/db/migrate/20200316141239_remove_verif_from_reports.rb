class RemoveVerifFromReports < ActiveRecord::Migration[6.0]
  def change
  	  	  	remove_column :reports, :verif 

  end
end
