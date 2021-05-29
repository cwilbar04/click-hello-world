# Simple Click CLI Integration

Click CLI tool for greeting.

Options:
--name: required, prompts if not entered. Name to greet. 
--excited: optional. Makes punctuation in to exclamation point.
--spanish: optional. Convert greeting to Spanish 'Hola'.
--shout: optional. Conver to all uppercase.

Usage Examples:

```cmd
greeting
```
Expected output:  
Prompts user for name.  
Output: Hello {Entered Name}.  
  
```cmd
greeting --name=Chris --excited --spanish --shout
```
Expected output:  
HOLA CHRIS!  
  
```cmd
greeting --excited
```
Expected output:  
Prompts user for name.  
Returns: Hello {Entered Name}!  
