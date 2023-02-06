# The DOCTYPE

Every HTML page starts with a doctype declaration.

The doctype’s purpose is to tell the browser what version of HTML it should use to render the document. The latest version of HTML is HTML5, and the doctype for that version is simply:

```html
<!DOCTYPE html>
```

The doctypes for older versions of HTML were a bit more complicated. For example, this is the doctype declaration for HTML4:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
```

However, we probably won’t ever want to be using an older version of HTML, and so we’ll always use:

```html
<!DOCTYPE html>
```
