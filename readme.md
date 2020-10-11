### REST end point query lanage

REST query language
### Grammar

```bash
input          = or, EOF;
or             = and, { "," , and };
and            = constraint, { ";" , constraint };
constraint     = ( group | comparison );
group          = "(", or, ")";
```
```bash
arguments      = ( "(", value, { "," , value }, ")" ) | value;
value          = unreserved-str | double-quoted | single-quoted;

unreserved-str = unreserved, { unreserved }
single-quoted  = "'", { ( escaped | all-chars - ( "'" | "\" ) ) }, "'";
double-quoted  = '"', { ( escaped | all-chars - ( '"' | "\" ) ) }, '"';

reserved       = '"' | "'" | "(" | ")" | ";" | "," | "=" | "!" | "~" | "<" | ">";
unreserved     = all-chars - reserved - " ";
escaped        = "\", all-chars;
all-chars      = ? all unicode characters ?;
```


### Example

```
- name=="Blah Singh";year=gt=2003
- name=="Foo" and year>2003
- genres=in=(commedy,action);genres=out=(romance,animated,horror),director==Something*blah
```