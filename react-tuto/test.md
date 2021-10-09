#  Test

# #  What to test

Test isolated unit, Test conditional output

For example, test `Log Out` button is shown after user logs in.

# #  Enzyme

A tool to test React Component

* shallow

    test the component, and **not assert** its child components

    ```javascript
    const wrapper = shallow(<NavItems />);
    wrapper.setProps({isLogIn: true});
    expect(wrapper.contains(<LogOutButton />)).toEqual(true);
    ```