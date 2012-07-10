# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Upcoming Plum Village Events</h1>

<ul id="events">
% if events:
  % for event in events:
  <li>
    <span class="text">${event['text']}</span>
    </span>
  </li>
  % endfor
% else:
  <li>There are no upcoming events</li>
% endif
</ul>

