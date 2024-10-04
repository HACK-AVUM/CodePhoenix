# tools/formatting_tool.py

class FormattingTool:
    def __init__(self, format_type='markdown'):
        self.format_type = format_type

    def format_report(self, analysis_data):
        if self.format_type == 'markdown':
            return self._format_as_markdown(analysis_data)
        elif self.format_type == 'html':
            return self._format_as_html(analysis_data)
        else:
            raise ValueError(f"Unsupported format type: {self.format_type}")

    def _format_as_markdown(self, analysis_data):
        report = "# Code Quality Report\n"
        for issue in analysis_data['issues']:
            report += f"## {issue['severity']}: {issue['message']}\n"
            report += f"  - File: {issue['file']}, Line: {issue['line']}\n"
            report += f"  - Description: {issue['description']}\n"
        return report

    def _format_as_html(self, analysis_data):
        report = "<h1>Code Quality Report</h1>\n"
        for issue in analysis_data['issues']:
            report += f"<h2>{issue['severity']}: {issue['message']}</h2>\n"
            report += f"<p>File: {issue['file']}, Line: {issue['line']}</p>\n"
            report += f"<p>Description: {issue['description']}</p>\n"
        return report
