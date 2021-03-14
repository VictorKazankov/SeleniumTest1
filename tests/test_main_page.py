def test_user_able_specify_age_for_one_child(main_page):
    main_page.open_change_number_guests_panel()
    main_page.increase_number_children()
    main_page.is_displayed_age_child_input()
    main_page.is_value_age_child_by_defult()


def test_user_able_specify_age_for_several_child(main_page):
    # set up count child here
    count_children = 4
    main_page.open_change_number_guests_panel()
    for child in range(count_children):
        main_page.increase_number_children()
    main_page.count_age_child_inputs(count_children)
