# import os
# import httplib2
# import matplotlib.pyplot as plt
# from googleapiclient.discovery import build
# from oauth2client.service_account import ServiceAccountCredentials

# def get_ga_metrics(medium=['ad'], source=['facebook']):
#     # Remember the JSON file you downloaded? We will use it now
#     # for oauth2 authentication. Be sure it's available on this
#     # path.
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(
#         os.path.join(os.path.dirname(__file__), 
#                       r'D:\T.tech website\myproject\myapp\credentials.json', ),
#         'https://www.googleapis.com/auth/analytics.readonly',
#     )
#     http = credentials.authorize(httplib2.Http())
    
#     # The URL of the discovery service.
#     DISCOVERY_URI = 'https://analyticsreporting.googleapis.com/$discovery/rest'
    
#     # Build the API connection.
#     analytics = build(
#         'analytics', 'v4', http=http, 
#         discoveryServiceUrl=DISCOVERY_URI)
    
#     # Define the query to get metrics like sessions, pageviews, and bounce rate
#     reports = analytics.reports().batchGet(
#         body={
#             'reportRequests': [
#                 {
#                     'viewId': '458555352',  # Replace with your view ID
#                     'dateRanges': [
#                         {'startDate': '2023-01-01', 'endDate': '2023-12-31'},
#                     ],
#                     'metrics': [
#                         {'expression': 'ga:sessions'},
#                         {'expression': 'ga:pageviews'},
#                         {'expression': 'ga:bounceRate'},
#                     ],
#                     'dimensions': [
#                         {'name': 'ga:medium'},
#                         {'name': 'ga:source'},
#                     ],
#                     "dimensionFilterClauses": [
#                         {
#                             "filters": [
#                                 {
#                                     "dimensionName": 'ga:medium',
#                                     "operator": 'EXACT',
#                                     "expressions": medium,
#                                 },
#                                 {
#                                     "dimensionName": 'ga:source',
#                                     "operator": 'EXACT',
#                                     "expressions": source,
#                                 },
#                             ],
#                         }
#                     ],
#                 }
#             ]
#         }
#     ).execute()
    
#     # Process the data and prepare for infographics
#     metrics = {'sessions': [], 'pageviews': [], 'bounceRate': []}
#     sources = []

#     for row in reports['reports'][0]['data'].get('rows', []):
#         sources.append(row['dimensions'][1])
#         metrics['sessions'].append(int(row['metrics'][0]['values'][0]))
#         metrics['pageviews'].append(int(row['metrics'][0]['values'][1]))
#         metrics['bounceRate'].append(float(row['metrics'][0]['values'][2]))

#     # Generate infographics (charts)
#     generate_infographics(metrics, sources)


# def generate_infographics(metrics, sources):
#     # Plot sessions vs pageviews and bounce rate
#     fig, axes = plt.subplots(1, 2, figsize=(14, 7))

#     # Plot 1: Sessions vs Pageviews
#     axes[0].bar(sources, metrics['sessions'], label='Sessions', color='blue', alpha=0.6, width=0.4, align='center')
#     axes[0].bar(sources, metrics['pageviews'], label='Pageviews', color='green', alpha=0.6, width=0.4, align='edge')
#     axes[0].set_title('Sessions vs Pageviews')
#     axes[0].set_xlabel('Source')
#     axes[0].set_ylabel('Count')
#     axes[0].legend()

#     # Plot 2: Bounce Rate
#     axes[1].bar(sources, metrics['bounceRate'], color='red', alpha=0.6)
#     axes[1].set_title('Bounce Rate')
#     axes[1].set_xlabel('Source')
#     axes[1].set_ylabel('Bounce Rate (%)')

#     # Show the plot
#     plt.tight_layout()
#     plt.show()


# # Example usage
# get_ga_metrics(medium=['ad'], source=['facebook'])
