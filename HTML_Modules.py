#!/usr/local/bin/python3
# Name: August Brenner
# File name: HTML_Modules.py
# Date: July 8th, 2013


# module for generating header HTML
def HTML_START(title):
    HTML_START = """
    <html>
        <head>
            <style type='text/css'>
                td {
                    text-align: right;
                    padding-left: 0.5em;
                    padding-right: 0.5em;
                }
                #top-nav ul li {
                    display: inline;
                    padding-right: 1em;
                }
            </style>
        </head>
        <body>
            <div id="top-nav">
                <ul>
                   <li><a href="rps_single_match">Single Match</a></li>
                   <li><a href="rps_tournament">Tournament</a></li>
                </ul>
            </div>
            <p>********** """ + title + """ **********</p>
    """
    print(HTML_START)


def HTML_END():
    print("""
        </body>
    </html>
    """)
