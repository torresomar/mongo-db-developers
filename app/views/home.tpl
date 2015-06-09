<!DOCTYPE html>
<html>
  <head>
    <title>Title of the document</title>
  </head>
<body>
  <p> Welcome Paps {{username}} </p>
  <ul>
    %for thing in things:
      <li>{{thing}}</li>
    %end
  </ul>
  <form action='/favorite_fruit' method='POST'>
    What type of fruit is your favorite?
    <input type="text" name="fruit" size="40" value="">
    <br>
    <input type="submit" value="Submit this fruit">
  </form>
</body>
</html>
