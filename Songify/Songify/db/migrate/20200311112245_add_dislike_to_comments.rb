class AddDislikeToComments < ActiveRecord::Migration[6.0]
  def change
    add_column :comments, :dislike, :integer
  end
end
