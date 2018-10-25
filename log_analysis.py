#! /usr/bin/env python

import psycopg2

DBNAME = "news"


def get_query_results(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows

    
query1 = """
    SELECT articles.title, COUNT(*) AS num
    FROM articles
    JOIN log
    ON log.path LIKE concat('/article/%', articles.slug)
    GROUP BY articles.title
    ORDER BY num DESC
    LIMIT 3;
    """

    
query2 = """
    SELECT authors.name, COUNT(*) AS num
    FROM authors
    JOIN articles
    ON authors.id = articles.author
    JOIN log
    ON log.path like concat('/article/%', articles.slug)
    GROUP BY authors.name
    ORDER BY num DESC
    LIMIT 3;
"""


query3 = """
    SELECT total.day,
      ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
    FROM (
      SELECT date_trunc('day', time) "day", count(*) AS error_requests
      FROM log
      WHERE status LIKE '404%'
      GROUP BY day
    ) AS errors
    JOIN (
      SELECT date_trunc('day', time) "day", count(*) AS requests
      FROM log
      GROUP BY day
      ) AS total
    ON total.day = errors.day
    WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
    ORDER BY percent DESC;
"""

requests1 = "What are the most popular articles of all time?"
requests2 = "Who are the most popular article authors of all time?"
requests3 = "On which datas more than 1% of the requests led to error?"


results1 = get_query_results(query1)
results2 = get_query_results(query2)
results3 = get_query_results(query3)

def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
print("\n")

print(request1)
print_results(result1)
print(request2)
print_results(result2)
print(request3)
print("\t" + result3[0][1] + " - " + str(result3[0][0]) + "%")
