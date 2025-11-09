#!/usr/bin/env python3
import re

# Read the backup file
with open('LRD-ECONAN-Herontwerp-2025.md.backup', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the mapping for main sections (## X.)
section_mapping = {
    '## 1. FUNCTIONAL': '## 2. FUNCTIONAL',
    '## 2. NON-FUNCTIONAL': '## 3. NON-FUNCTIONAL',
    '## 3. ASSESSMENT': '## 4. ASSESSMENT',
    '## 4. SUPPORT': '## 5. SUPPORT',
    '## 5. CONTENT': '## 6. CONTENT',
    '## 6. MEASUREMENT': '## 7. MEASUREMENT',
    '## 7. ITERATION': '## 8. ITERATION',
    '## 8. RISK': '## 9. RISK',
    '## 9. SUCCESS': '## 10. SUCCESS',
    '## 10. IMPLEMENTATION': '## 11. IMPLEMENTATION',
    '## 11. ROLES': '## 12. ROLES',
    '## 12. APPENDICES': '## 13. APPENDICES',
}

# Apply main section replacements
for old, new in section_mapping.items():
    content = content.replace(old, new)

# Now fix subsections based on their parent section
# Section 2 (was 1) - FUNCTIONAL REQUIREMENTS
content = re.sub(r'### 1\.1 Purpose', '### 2.1 Purpose', content)
content = re.sub(r'### 1\.2 Autonomy', '### 2.2 Autonomy', content)
content = re.sub(r'### 1\.3 Mastery', '### 2.3 Mastery', content)

# Section 3 (was 2) - NON-FUNCTIONAL
content = re.sub(r'### 2\.1 Quality', '### 3.1 Quality', content)
content = re.sub(r'### 2\.2 Scalability', '### 3.2 Scalability', content)
content = re.sub(r'### 2\.3 Workload', '### 3.3 Workload', content)

# Section 4 (was 3) - ASSESSMENT
content = re.sub(r'### 3\.1 Assessment Criteria', '### 4.1 Assessment Criteria', content)
content = re.sub(r'### 3\.2 Differentiation', '### 4.2 Differentiation', content)

# Section 5 (was 4) - SUPPORT
content = re.sub(r'### 4\.1 Student Support', '### 5.1 Student Support', content)
content = re.sub(r'### 4\.2 Docent Support', '### 5.2 Docent Support', content)

# Section 6 (was 5) - CONTENT & STRUCTURE
content = re.sub(r'### 5\.1 Module Structure', '### 6.1 Module Structure', content)
content = re.sub(r'### 5\.2 Learning Materials', '### 6.2 Learning Materials', content)

# Section 7 (was 6) - MEASUREMENT & EVALUATION
content = re.sub(r'### 6\.1 Real-Time', '### 7.1 Real-Time', content)
content = re.sub(r'### 6\.2 End-of-Module', '### 7.2 End-of-Module', content)
content = re.sub(r'### 6\.3 Long-Term', '### 7.3 Long-Term', content)

# Section 8 (was 7) - ITERATION
content = re.sub(r'### 7\.1 Pilot Approach', '### 8.1 Pilot Approach', content)
content = re.sub(r'### 7\.2 Iteration Process', '### 8.2 Iteration Process', content)
content = re.sub(r'### 7\.3 Continuous', '### 8.3 Continuous', content)

# Section 9 (was 8) - RISK
content = re.sub(r'### 8\.1 Identified Risks', '### 9.1 Identified Risks', content)

# Section 10 (was 9) - SUCCESS METRICS
content = re.sub(r'### 9\.1 Primary', '### 10.1 Primary', content)
content = re.sub(r'### 9\.2 Secondary', '### 10.2 Secondary', content)
content = re.sub(r'### 9\.3 Leading', '### 10.3 Leading', content)

# Section 11 (was 10) - IMPLEMENTATION
content = re.sub(r'### 10\.1 Phase 1', '### 11.1 Phase 1', content)
content = re.sub(r'### 10\.2 Phase 2', '### 11.2 Phase 2', content)
content = re.sub(r'### 10\.3 Phase 3', '### 11.3 Phase 3', content)
content = re.sub(r'### 10\.4 Phase 4', '### 11.4 Phase 4', content)
content = re.sub(r'### 10\.5 Phase 5', '### 11.5 Phase 5', content)

# Write the corrected content
with open('LRD-ECONAN-Herontwerp-2025.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Section numbers fixed successfully!")
