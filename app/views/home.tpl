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
</body>
</html>
