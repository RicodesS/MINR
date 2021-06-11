class AddFavoritesUser < ActiveRecord::Migration[6.0]
  def change
  	    add_column :users, :favorites, :text , array: true
  end
end
