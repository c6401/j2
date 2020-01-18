# J2

Shell tool to render jinja template files:

```sh
j2 my_template.txt.j2  
```
This will create my_template.txt rendered with jinja, the file will be rerenderd on every detected template change while j2 is running.

It also supports frontmatter:
```jinja2
---
text: hello world
---
{{ text }}
```
will produce:
```
hello world
```
