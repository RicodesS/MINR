require 'test_helper'

class ConcertsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @concert = concerts(:one)
  end

  test "should get index" do
    get concerts_url
    assert_response :success
  end

  test "should get new" do
    get new_concert_url
    assert_response :success
  end

  test "should create concert" do
    assert_difference('Concert.count') do
      post concerts_url, params: { concert: { id: @concert.id, name: @concert.name, venue: @concert.venue } }
    end

    assert_redirected_to concert_url(Concert.last)
  end

  test "should show concert" do
    get concert_url(@concert)
    assert_response :success
  end

  test "should get edit" do
    get edit_concert_url(@concert)
    assert_response :success
  end

  test "should update concert" do
    patch concert_url(@concert), params: { concert: { id: @concert.id, name: @concert.name, venue: @concert.venue } }
    assert_redirected_to concert_url(@concert)
  end

  test "should destroy concert" do
    assert_difference('Concert.count', -1) do
      delete concert_url(@concert)
    end

    assert_redirected_to concerts_url
  end
end
