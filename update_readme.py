
import datetime

def update_readme():
    # Read the existing README.md file
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and remove any existing "Last Updated" lines
    lines = content.split('\n')
    lines = [line for line in lines if 'Last Updated' not in line]

    # Add a new "Last Updated" line with the current timestamp
    last_updated = f"Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    lines.append('')
    lines.append(last_updated)

    # Write the updated content back to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == '__main__':
    update_readme()
