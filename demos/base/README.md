# Base Demo Template

These files define the base for an Emily demo to ensure consistent presentation.

## Prerequisites
A SCSS pre-compiler. In VS Code, install the `Live Sass Compiler` extension, press CMD + SHIFT + P and run `Live Sass: Watch Sass`. The extension will automatically compile the `*/**/*.scss` files into `.css` files when you change them.

## Quick start
```
python3 -m http.server 8000
```

Open http://localhost:8000 in your browser.

## Content
Your content goes into `index.html`:
```html
...
        <section class="content">
            <!-- INSERT CONTENT HERE -->

            <h2>Your content goes here</h2>
            ...

        </section>
... 
```

## Styling
Declare your styling rules in `./styles/content.scss`. 
Consult `./styles/variables/variables.scss` for a set of color variables that you can use.
Consult `./styles/base/base.scss` for the base styling that is applied to the entire document.

## Scripting
Put your code in `./scripts/script.js`. The code is interpreted when the page is loaded.