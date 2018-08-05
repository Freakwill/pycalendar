
command: 'python3 pycalendar/script.py'

#Set this to true to enable previous and next month dates, or false to disable
otherMonths: true

refreshFrequency: 3600000

style: """
  top: 10px
  right: 10px
  color: #FF99FF
  font-family: Helvetica Neue
  background: rgba(pink, 0.4)
  background-size: 176px 84px

  table
    border-collapse: collapse
    table-layout: fixed

  td
    text-align: center
    padding: 4px 6px
    text-shadow: 0 0 1px rgba(#000, 0.5)

  div
    text-align: center
    color: pink

  thead tr
    &:first-child td
      font-size: 24px
      font-weight: 100
      color: orange

    &:last-child td
      font-size: 11px
      padding-bottom: 10px
      font-weight: 500

  tbody td
    font-size: 12px

  .today
    font-weight: bold
    background: rgba(#fff, 0.2)
    border-radius: 50%
    color: red

  .grey
    color: rgba(#C0C0C0, .7)

  .weekend
    color: yellow
"""

render: (output) ->

  output = output.split(";")
  today = output[0]
  cal = output[1]
  """
      #{cal}
  """


updateCal: (cal, today, table) ->
  [month, date, year] = today.split('-')

  """
  #{date}
  #{table}
  """

update: (output, domEl) ->
  output = output.split(";")
  today = output[0]
  cal = output[1]
  table = $(domEl)

  @updateCal cal, today, table
