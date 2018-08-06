
command: 'python3 pycalendar/script.py'

#Set this to true to enable previous and next month dates, or false to disable
otherMonths: true

refreshFrequency: '12h'

style: """
  top: 10px
  right: 10px
  font-family: Helvetica Neue
  background: rgba(pink, 0.4)
  background-size: 176px 84px

  table
    text-align: center

  th
    font-size: 12px
    font-weight: 300
    color: red

    &.month
      color: purple
      font-size: 15px
      font-weight: 400

    &.su
    &.sa
      color: orange

  td
    padding: 4px 6px
    text-shadow: 0 0 1px rgba(#000, 0.5)
    font-size: 12px
    color: blue
      
  .today
    font-weight: bold
    background: rgba(#fff, 0.2)
    border-radius: 50%
    color: red

  .grey
    color: rgba(#C0C0C0, .7)

"""

render: (output) ->

  output = output.split(";;")
  today = output[0]
  cal = output[1]
  """
      #{cal}
  """


# updateCal: (cal, today, table) ->
#   [month, date, year] = today.split('-')

#   """
#   #{date}
#   #{table}
#   """

# update: (output, domEl) ->
#   output = output.split(";")
#   today = output[0]
#   cal = output[1]
#   table = $(domEl)

#   @updateCal cal, today, table
