test




<svg width="1400" height="1000" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="triggerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9b59b6;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8e44ad;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="clientGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e74c3c;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#c0392b;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="serverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3498db;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2980b9;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="toolGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2ecc71;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#27ae60;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="resourceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f39c12;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e67e22;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="outputGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#34495e;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2c3e50;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="1400" height="1000" fill="#f8f9fa"/>
  
  <!-- Title -->
  <text x="700" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="#2c3e50">Smart CSV Processing MCP Architecture</text>
  <text x="700" y="65" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="#7f8c8d">Model Context Protocol • Autonomous Processing • Zero-Touch Operations</text>
  
  <!-- Layer Labels -->
  <rect x="20" y="105" width="120" height="35" rx="17" fill="#34495e"/>
  <text x="80" y="127" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">🚀 TRIGGERS</text>
  
  <rect x="20" y="205" width="120" height="35" rx="17" fill="#34495e"/>
  <text x="80" y="227" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">🧠 MCP CLIENT</text>
  
  <rect x="20" y="305" width="120" height="35" rx="17" fill="#34495e"/>
  <text x="80" y="327" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">⚙️ MCP SERVERS</text>
  
  <rect x="20" y="455" width="120" height="35" rx="17" fill="#34495e"/>
  <text x="80" y="477" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">🔧 TOOLS</text>
  
  <rect x="20" y="555" width="120" height="35" rx="17" fill="#34495e"/>
  <text x="80" y="577" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">💾 RESOURCES</text>
  
  <rect x="20" y="705" width="120" height="35" rx="17" fill="#34495e"/>
  <text x="80" y="727" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">📤 OUTPUTS</text>
  
  <!-- TRIGGERS Layer -->
  <rect x="200" y="100" width="180" height="80" rx="12" fill="url(#triggerGrad)" filter="url(#shadow)"/>
  <text x="290" y="125" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">📁 File System</text>
  <text x="290" y="142" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Directory watchers</text>
  <text x="290" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">New file detection</text>
  <text x="290" y="168" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Format validation</text>
  
  <rect x="420" y="100" width="180" height="80" rx="12" fill="url(#triggerGrad)" filter="url(#shadow)"/>
  <text x="510" y="125" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">📡 API Endpoints</text>
  <text x="510" y="142" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">REST uploads</text>
  <text x="510" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Webhook receivers</text>
  <text x="510" y="168" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Batch submissions</text>
  
  <rect x="640" y="100" width="180" height="80" rx="12" fill="url(#triggerGrad)" filter="url(#shadow)"/>
  <text x="730" y="125" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">⏰ Scheduled Jobs</text>
  <text x="730" y="142" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Cron triggers</text>
  <text x="730" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Periodic imports</text>
  <text x="730" y="168" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Time-based processing</text>
  
  <!-- Arrow 1 -->
  <polygon points="700,190 690,200 710,200" fill="#95a5a6"/>
  
  <!-- MCP CLIENT Layer -->
  <rect x="350" y="200" width="400" height="80" rx="12" fill="url(#clientGrad)" filter="url(#shadow)"/>
  <text x="550" y="225" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="white">🤖 Autonomous Decision Engine</text>
  <text x="550" y="242" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">LLM-Powered Intelligence • Schema Analysis • Routing Decisions</text>
  <text x="550" y="255" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Batch Processing Logic • Error Classification • Tool Orchestration</text>
  
  <!-- Arrow 2 -->
  <polygon points="550,290 540,300 560,300" fill="#95a5a6"/>
  
  <!-- MCP SERVERS Layer -->
  <rect x="200" y="300" width="160" height="80" rx="12" fill="url(#serverGrad)" filter="url(#shadow)"/>
  <text x="280" y="320" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="white">📊 CSV Analyzer</text>
  <text x="280" y="335" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">File validation</text>
  <text x="280" y="348" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Schema detection</text>
  <text x="280" y="361" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Column mapping</text>
  <text x="280" y="374" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Data type inference</text>
  
  <rect x="380" y="300" width="160" height="80" rx="12" fill="url(#serverGrad)" filter="url(#shadow)"/>
  <text x="460" y="325" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="white">🗄️ Database Handler</text>
  <text x="460" y="342" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Connection pooling</text>
  <text x="460" y="355" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Transaction management</text>
  <text x="460" y="368" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Batch operations</text>
  
  <rect x="560" y="300" width="160" height="80" rx="12" fill="url(#serverGrad)" filter="url(#shadow)"/>
  <text x="640" y="325" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="white">📝 Logger</text>
  <text x="640" y="342" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Event tracking</text>
  <text x="640" y="355" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Error reporting</text>
  <text x="640" y="368" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Audit trails</text>
  
  <rect x="740" y="300" width="160" height="80" rx="12" fill="url(#serverGrad)" filter="url(#shadow)"/>
  <text x="820" y="325" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="white">📂 File Manager</text>
  <text x="820" y="342" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Move operations</text>
  <text x="820" y="355" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Archive handling</text>
  <text x="820" y="368" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white">Cleanup tasks</text>
  
  <!-- Arrow 3 -->
  <polygon points="550,390 540,400 560,400" fill="#95a5a6"/>
  
  <!-- Connection Lines from Servers to Resources -->
  <line x1="280" y1="380" x2="340" y2="500" stroke="#f39c12" stroke-width="2" opacity="0.7"/>
  <line x1="280" y1="380" x2="740" y2="500" stroke="#f39c12" stroke-width="2" opacity="0.7"/>
  
  <line x1="460" y1="380" x2="340" y2="500" stroke="#f39c12" stroke-width="2" opacity="0.7"/>
  
  <line x1="640" y1="380" x2="540" y2="500" stroke="#f39c12" stroke-width="2" opacity="0.7"/>
  <line x1="640" y1="380" x2="740" y2="500" stroke="#f39c12" stroke-width="2" opacity="0.7"/>
  
  <line x1="820" y1="380" x2="540" y2="500" stroke="#f39c12" stroke-width="2" opacity="0.7"/>
  
  <!-- Connection Lines from Servers to Tools -->
  <line x1="280" y1="380" x2="210" y2="400" stroke="#3498db" stroke-width="2" opacity="0.7"/>
  <line x1="280" y1="380" x2="770" y2="400" stroke="#3498db" stroke-width="2" opacity="0.7"/>
  
  <line x1="460" y1="380" x2="350" y2="400" stroke="#3498db" stroke-width="2" opacity="0.7"/>
  
  <line x1="640" y1="380" x2="490" y2="400" stroke="#3498db" stroke-width="2" opacity="0.7"/>
  
  <line x1="820" y1="380" x2="630" y2="400" stroke="#3498db" stroke-width="2" opacity="0.7"/>
  
  <!-- TOOLS Layer -->
  <rect x="150" y="400" width="120" height="70" rx="10" fill="url(#toolGrad)" filter="url(#shadow)"/>
  <text x="210" y="420" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="white">🔍 validate_schema</text>
  <text x="210" y="435" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Column matching</text>
  <text x="210" y="448" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Type checking</text>
  <text x="210" y="461" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Validation rules</text>
  
  <rect x="290" y="400" width="120" height="70" rx="10" fill="url(#toolGrad)" filter="url(#shadow)"/>
  <text x="350" y="420" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="white">📥 load_batch</text>
  <text x="350" y="435" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Transaction control</text>
  <text x="350" y="448" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Data insertion</text>
  <text x="350" y="461" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Rollback handling</text>
  
  <rect x="430" y="400" width="120" height="70" rx="10" fill="url(#toolGrad)" filter="url(#shadow)"/>
  <text x="490" y="420" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="white">📋 log_event</text>
  <text x="490" y="435" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Status tracking</text>
  <text x="490" y="448" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Error details</text>
  <text x="490" y="461" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Audit logging</text>
  
  <rect x="570" y="400" width="120" height="70" rx="10" fill="url(#toolGrad)" filter="url(#shadow)"/>
  <text x="630" y="420" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="white">📁 move_file</text>
  <text x="630" y="435" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">File relocation</text>
  <text x="630" y="448" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Archive management</text>
  <text x="630" y="461" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Cleanup operations</text>
  
  <rect x="710" y="400" width="120" height="70" rx="10" fill="url(#toolGrad)" filter="url(#shadow)"/>
  <text x="770" y="420" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="white">🎯 match_table</text>
  <text x="770" y="435" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Smart routing</text>
  <text x="770" y="448" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Target selection</text>
  <text x="770" y="461" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="white">Confidence scoring</text>
  
  <!-- Arrow 4 -->
  <polygon points="550,480 540,490 560,490" fill="#95a5a6"/>
  
  <!-- RESOURCES Layer -->
  <rect x="250" y="500" width="180" height="80" rx="12" fill="url(#resourceGrad)" filter="url(#shadow)"/>
  <text x="340" y="525" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">🏛️ Target Databases</text>
  <text x="340" y="542" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">PostgreSQL, Oracle</text>
  <text x="340" y="555" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">MySQL, SQL Server</text>
  <text x="340" y="568" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Table schemas</text>
  
  <rect x="450" y="500" width="180" height="80" rx="12" fill="url(#resourceGrad)" filter="url(#shadow)"/>
  <text x="540" y="525" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">📂 File System</text>
  <text x="540" y="542" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Input directories</text>
  <text x="540" y="555" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Archive folders</text>
  <text x="540" y="568" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Error queues</text>
  
  <rect x="650" y="500" width="180" height="80" rx="12" fill="url(#resourceGrad)" filter="url(#shadow)"/>
  <text x="740" y="525" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">⚙️ Configuration</text>
  <text x="740" y="542" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Connection strings</text>
  <text x="740" y="555" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Processing rules</text>
  <text x="740" y="568" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Validation settings</text>
  
  <!-- Arrow 5 -->
  <polygon points="550,590 540,600 560,600" fill="#95a5a6"/>
  
  <!-- OUTPUTS Layer -->
  <rect x="350" y="650" width="180" height="80" rx="12" fill="url(#outputGrad)" filter="url(#shadow)"/>
  <text x="440" y="675" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">✅ Processed</text>
  <text x="440" y="692" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Successful loads</text>
  <text x="440" y="705" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Archive folder</text>
  <text x="440" y="718" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Success metrics</text>
  
  <rect x="550" y="650" width="180" height="80" rx="12" fill="url(#outputGrad)" filter="url(#shadow)"/>
  <text x="640" y="675" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white">❌ Unprocessed</text>
  <text x="640" y="692" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Failed validation</text>
  <text x="640" y="705" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Error folder</text>
  <text x="640" y="718" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="white">Detailed logs</text>
  
  <!-- Key Principles Box -->
  <rect x="900" y="150" width="480" height="580" rx="15" fill="white" stroke="#ecf0f1" stroke-width="2" filter="url(#shadow)"/>
  <text x="1140" y="180" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#2c3e50">🎯 Core Principles</text>
  
  <rect x="920" y="200" width="440" height="120" rx="8" fill="#ecf0f1"/>
  <text x="940" y="220" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#2c3e50">📁 File-Level Processing</text>
  <text x="940" y="240" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Each CSV file processed independently</text>
  <text x="940" y="255" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• One file failure doesn't affect others</text>
  <text x="940" y="270" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Per-file: all-or-nothing validation</text>
  <text x="940" y="285" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Failed files → unprocessed folder</text>
  <text x="940" y="300" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Successful files → processed folder</text>
  
  <rect x="920" y="340" width="440" height="120" rx="8" fill="#ecf0f1"/>
  <text x="940" y="360" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#2c3e50">🧠 Intelligent Schema Matching</text>
  <text x="940" y="380" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• LLM-powered column mapping</text>
  <text x="940" y="395" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Handles naming variations automatically</text>
  <text x="940" y="410" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Confidence-based table selection</text>
  <text x="940" y="425" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Data type validation and inference</text>
  <text x="940" y="440" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Exact schema alignment required</text>
  
  <rect x="920" y="480" width="440" height="120" rx="8" fill="#ecf0f1"/>
  <text x="940" y="500" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#2c3e50">⚡ Autonomous Operations</text>
  <text x="940" y="520" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Zero human intervention required</text>
  <text x="940" y="535" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Self-healing error handling</text>
  <text x="940" y="550" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Intelligent batch processing</text>
  <text x="940" y="565" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Comprehensive audit logging</text>
  <text x="940" y="580" font-family="Arial, sans-serif" font-size="12" fill="#7f8c8d">• Real-time monitoring and alerts</text>
  
  <rect x="920" y="620" width="440" height="100" rx="8" fill="#ecf0f1"/>
  <text x="940" y="640" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#2c3e50">🔗 Server Connections</text>
  <text x="940" y="658" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#3498db">Tools (Blue Lines):</text>
  <text x="940" y="672" font-family="Arial, sans-serif" font-size="10" fill="#7f8c8d">CSV Analyzer→validate_schema,match_table | DB Handler→load_batch</text>
  <text x="940" y="684" font-family="Arial, sans-serif" font-size="10" fill="#7f8c8d">Logger→log_event | File Manager→move_file</text>
  <text x="940" y="698" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#f39c12">Resources (Orange Lines):</text>
  <text x="940" y="712" font-family="Arial, sans-serif" font-size="10" fill="#7f8c8d">CSV Analyzer→Databases,Config | DB Handler→Databases</text>
  <text x="940" y="724" font-family="Arial, sans-serif" font-size="10" fill="#7f8c8d">Logger→File System,Config | File Manager→File System</text>
</svg>
