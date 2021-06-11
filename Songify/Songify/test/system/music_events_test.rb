require "application_system_test_case"

class MusicEventsTest < ApplicationSystemTestCase
  setup do
    @music_event = music_events(:one)
  end

  test "visiting the index" do
    visit music_events_url
    assert_selector "h1", text: "Music Events"
  end

  test "creating a Music event" do
    visit music_events_url
    click_on "New Music Event"

    fill_in "Body", with: @music_event.body
    fill_in "Title", with: @music_event.title
    click_on "Create Music event"

    assert_text "Music event was successfully created"
    click_on "Back"
  end

  test "updating a Music event" do
    visit music_events_url
    click_on "Edit", match: :first

    fill_in "Body", with: @music_event.body
    fill_in "Title", with: @music_event.title
    click_on "Update Music event"

    assert_text "Music event was successfully updated"
    click_on "Back"
  end

  test "destroying a Music event" do
    visit music_events_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Music event was successfully destroyed"
  end
end
