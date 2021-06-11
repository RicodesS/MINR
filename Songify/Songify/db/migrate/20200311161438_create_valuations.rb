class CreateValuations < ActiveRecord::Migration[6.0]
  def change
    create_table :valuations do |t|
      t.integer :value, :default=>0
      t.string :artist
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end
  end
end
