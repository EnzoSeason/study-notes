#  Animation

# #  CSS transition

[css transition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)

```html
<div class="container">
    {
        isOpen
        ? <div class="open"></div>
        : <div class="close"></div>
    }
</div>
```

```css
.container {
    transition: all 0.3s ease-out;
}

.open {
    transform: translateY(0);
}

.close {
    transform: translateY(-100%);
}
```

# #  CSS @keyframe

To fine-tune the animation, use `@keyframe` and `animation`

```css
@keyframe openModal {
    0% {
        transform: translateY(-100%);
    },
    50% {
        transform: translateY(50%);
    },
    100% {
        transform: translateY(0%);
    }
}
```

```css
.open {
    animation: openModal 0.3s ease-out forwards;
}
```

# #  react-transition-group

A package of React for animation. It's mostly for adding or removing elements to / from the DOM.

[doc](http://reactcommunity.org/react-transition-group/)

# #  Other packages

* [React-motion](https://github.com/chenglou/react-motion): for physical simulation

* [React-move](https://react-move.js.org/# /): for BI animation