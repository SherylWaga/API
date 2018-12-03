# iReporter

[![Build Status](https://travis-ci.org/SherylWaga/API.svg?branch=develop)](https://travis-ci.org/SherylWaga/API)
[![Coverage Status](https://coveralls.io/repos/github/SherylWaga/API/badge.svg?branch=ch-implement-Travis-162341102)](https://coveralls.io/github/SherylWaga/API?branch=ch-implement-Travis-162341102)
[![Maintainability](https://api.codeclimate.com/v1/badges/bd2ec3ecdf59e3451b49/maintainability)](https://codeclimate.com/github/SherylWaga/API/maintainability)

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

## Prerequisites
Things you need to run the application;
* Requirements
* virtual environment

` python3 -m venv venv `

` pip install -r requirements.txt `

## Installing
Clone my repository;

` git clone https://github.com/SherylWaga/API.git  `


## Running the tests
Run this command on terminal:

` pytests `

## Endpoints

You can run the urls on postman
<table >
<th>Method</th>
<th>Url</th>
<th>Description</th>
    <tr>
        <td>POST</td>
        <td> 127.0.0.1/api/v1/redflags  </td>
        <td>Create a Redflag </td>
    </tr>
     <tr>
        <td>GET</td>
         <td> 127.0.0.1/api/v1/redflags</td>
        <td>View Redflags </td>
    </tr>
    <tr>
        <td>GET</td>
         <td>127.0.0.1/api/v1/redflags/1 </td>
        <td>View specific redflag </td>
    </tr>
    <tr>
        <td>PUT</td>
         <td>127.0.0.1/api/v1/redflags/1 </td>
        <td>Edit comment and location of a redflag </td>
    </tr>
    <tr>
        <td>DELETE</td>
         <td>127.0.0.1/api/v1/redflags/1 </td>
        <td>Delete a Redflag </td>
    </tr>
</table>














