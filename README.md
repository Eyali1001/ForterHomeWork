# ForterHomeWork
solutions of challenges

for the first (javascript in IE6 challange) I used html_log to try and find out where the compression algorithm goes wrong. Turns out, the variables were being logged as undefined. I managed to find the problematic command using html_log in different locations:
```
context_c = uncompressed[ii];
```
After this command, context_c was undefined. I changed it to the first logical thing that popped in my head, the function .charAt:
```
context_c = uncompressed.charAt(ii); 
```
this produced the wanted results.
