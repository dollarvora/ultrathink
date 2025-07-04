class EmailTemplate:
    def render(self, role_summary, urgency_counts, total_items):
        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>ULTRATHINK Pricing Intelligence Digest</h2>
            <p><strong>Role:</strong> {role_summary['role']}</p>
            <p><strong>Focus:</strong> {role_summary.get('focus', 'N/A')}</p>
            <p><strong>Total Items:</strong> {total_items}</p>

            <h3>Urgency Breakdown</h3>
            <ul>
                <li><strong>High:</strong> {urgency_counts.get('high', 0)}</li>
                <li><strong>Medium:</strong> {urgency_counts.get('medium', 0)}</li>
                <li><strong>Low:</strong> {urgency_counts.get('low', 0)}</li>
            </ul>

            <h3>Executive Summary</h3>
            <p>{role_summary['summary']}</p>

            <h3>Key Insights</h3>
            <ul>
        """
        insights = role_summary.get('key_insights', [])
        if insights:
            for insight in insights:
                html += f"<li>{insight}</li>"
        else:
            html += f"<li>📊 No immediate action items detected for this role in the current analysis period</li>"

        html += "</ul><h3>Top Vendors</h3><ul>"
        for vendor in role_summary.get('top_vendors', []):
            highlight = ' style="font-weight:bold;"' if vendor.get('highlighted') else ''
            html += f"<li{highlight}>{vendor['vendor']}: {vendor['mentions']} mentions</li>"

        html += "</ul><h3>Sources</h3><ul>"
        for source, count in role_summary.get('sources', {}).items():
            html += f"<li>{source}: {count} items</li>"

        html += """
            </ul>
            <p style="margin-top: 30px; font-size: 12px; color: #777;">Generated by ULTRATHINK</p>
        </body>
        </html>
        """
        return html
