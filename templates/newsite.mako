# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Add a new site</h1>

<form action="${request.route_url('newsite')}" method="post">
  <input type="text" maxlength="200" name="name">
  <input type="submit" name="add" value="ADD" class="button">
</form>

