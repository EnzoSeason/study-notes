#  Styling

# #  style sheet

It's the most common way. But it's hard to change the style dynamically.

# # #  Button.js

```css
.Button {
  padding: 20px;
}
```

# # #  Button.js (v1)

```javascript
import React, { Component } from 'react';
import './Button.css'; // Tell webpack that Button.js uses these styles

class Button extends Component {
  render() {
    // You can use them as regular CSS styles
    return <div className="Button" />;
  }
}
```

# #  CSS Module (personnal favorite)

In JavaScript file, Read the css from style sheet

This project supports CSS Modules alongside regular stylesheets using the `[name].module.css` file naming convention. CSS Modules allows the scoping of CSS by automatically creating a unique classname of the format `[filename]\_[classname]\_\_[hash]`.

# # #  Button.module.css

MUST name the file ended by .module.css

```css
.Error {
  background-color: red;
}
```

# # #  Button.js (v2)

```javascript
import React, { Component } from 'react';
import styles from './Button.module.css'; // Import css modules stylesheet as styles

class Button extends Component {
  render() {
    // reference as a js object
    return <button className={styles.Error}>Error Button</button>;
  }
}
```

# #  redium

`npm install --save radium`

Radium can manipulate Media Queries, Pseudo selectors, ...

To use it:

```javascript
import Radium from 'redium';

export default Radium(MyComponent);
```

Pseudo selectors:

```javascript
const MyComponent = props => {
    const style = {
        ':hover': {
            backgroundColor: 'red'
        }
    };

    return (
        <div>
            // something
        </div>
    )
}
```

Media Queries

```javascript
const MyComponent = props => {
    const style = {
        '@media(min-width: 500px)': {
            width: '450px'
        }
    };

    return (
        <StyleRoot>
            <div>
                // something
            </div>
        </StyleRoot>
    );

}
```

# #  styled components

`npm install --save styled-components`

To use it:

```javascript
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;

  &:hover {
      backgroundColor: red
  }
`;

render(
    <Title>
        Hello World!
    </Title>
);
```
