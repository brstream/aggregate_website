# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Aggregate of URLs</h1>

<ul id="urls">
% if urls:
  % for item in urls:
  <li>
    <a href="${item['url']}">${item['text']}</a>
  </li>
  % endfor
% else:
  <li>There are no URLs</li>
% endif
  <li class="last">
    <a href="${request.route_url('newsite')}">Add a new URL</a>
  </li>
</ul>

