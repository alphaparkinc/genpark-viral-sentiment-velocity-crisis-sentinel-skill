from client import ViralSentimentVelocityCrisisSentinelClient

def main():
    client = ViralSentimentVelocityCrisisSentinelClient()
    res = client.evaluate_brand_mention_velocity('CloudShield Security', 12.5, 84.0)
    print('Crisis Sentinel: ' + res['crisis_alert_id'] + ' (' + res['viral_escalation_tier'] + ')')
    print('Holding Statement: ' + res['synthesized_holding_statement_text'])
    print('War Room: ' + res['incident_war_room_portal_url'])

if __name__ == '__main__':
    main()
