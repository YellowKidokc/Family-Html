import os

html_file = r"D:\GitHub\Family-Html\index.html"

zenodo_data = """
# FP Series
FP-015: Coherence Recovery Validation|https://zenodo.org/records/19346623
FP-014: Constitutional Audit|https://zenodo.org/records/19346550
FP-010: Fruits of the Spirit as Coherence Diagnostics|https://zenodo.org/records/19346482
FP-002A: Bias and Assumptions|https://zenodo.org/records/19346297
FP-007: The 7Q Framework|https://zenodo.org/records/19346158

# FT Series
FT-016: Master Equation Verification|https://zenodo.org/records/19185596
FT-015: The Equation That Wouldn't Break|https://zenodo.org/records/19172625
FT-014: The Same Equation Everywhere|https://zenodo.org/records/19172467
FT-013: BAES AI Evaluation System|https://zenodo.org/records/19172294
FT-012: Temporality as Operational Domain|https://zenodo.org/records/19172178
FT-011: Terminus Sui|https://zenodo.org/records/19172176
FT-010: The Nucleation Thesis|https://zenodo.org/records/19171981
FT-009: The Adversary Thread|https://zenodo.org/records/19171850
FT-008: The Hubble Gradient Distance|https://zenodo.org/records/18868269
FT-007: Unforced Consensus|https://zenodo.org/records/19171673
FT-006: The Pharisee Function|https://zenodo.org/records/18869887
FT-005: The Trinity Requirement|https://zenodo.org/records/19171600
FT-004: Turtles and the Floor|https://zenodo.org/records/19171377
FT-003: Math Is Moral|https://zenodo.org/records/19171197
FT-002: Math Before Matter|https://zenodo.org/records/19171073
FT-001: Truth Measurement Method|https://zenodo.org/records/19170903

# SP Series
SP-17: The Inverse Solver|https://zenodo.org/records/19193512
SP-16: The Configuration Ladder|https://zenodo.org/records/19188615
SP-15: Sutherland Polymerization|https://zenodo.org/records/19188525
SP-14: 1000 Genomes Fixation Analysis|https://zenodo.org/records/19188399
SP-13: RNA World Bootstrap Problem|https://zenodo.org/records/19187920
SP-12: Miller Chemistry-Information Gap|https://zenodo.org/records/19187791
SP-11: Gillespie DFE Mismatch|https://zenodo.org/records/19187708
SP-10: Green Neanderthal Introgression|https://zenodo.org/records/19187618
SP-09: Eyre-Walker DFE Stability|https://zenodo.org/records/19187533
SP-08: Maynard Smith Protein Space|https://zenodo.org/records/19187410
SP-07: Heath FBD Assumptions|https://zenodo.org/records/19187194
SP-06: Blount Citrate|https://zenodo.org/records/19163529
SP-05: Cambrian Lynch-Abegg Analysis|https://zenodo.org/records/19160874
SP-04: Kimura DFE Tension|https://zenodo.org/records/19186999
SP-03: Computational Model Circularity|https://zenodo.org/records/19160022
SP-02: Barrick LTEE Mismatch|https://zenodo.org/records/19159946
SP-01: Haldane's Rate Problem|https://zenodo.org/records/19159631

# Formal Treatments
Theophysics Complete Formal Treatment|https://zenodo.org/records/19193734
Pure Formal Layer Mathematical Foundation|https://zenodo.org/records/19193669
Structural Isomorphism Between Physical and Moral Law|https://zenodo.org/records/19194010
Self-Enclosed Systems and Structural Incompleteness|https://zenodo.org/records/19193914
A Scalar Field Theory with Non-Minimal Gravitational Coupling|https://zenodo.org/records/19193835
Formal Theophysics Complete Paper Series|https://zenodo.org/records/19172716
"""

output_html = """
        <!-- Zenodo Archive -->
        <div class="section-label" style="margin-top: 4rem;">The Zenodo Archive</div>
        <p style="color: var(--text-dim); font-size: 0.9rem; margin-bottom: 2rem; max-width: 800px;">
            The complete repository of historical derivations, structural claims, and formal audits. Evey paper is permanently archived at CERN's Zenodo with an assigned Digital Object Identifier (DOI).
        </p>
        
        <div style="display: flex; flex-direction: column; gap: 2.5rem; margin-bottom: 4rem;">
"""

current_section = ""
for line in zenodo_data.strip().split('\n'):
    line = line.strip()
    if not line: continue
    if line.startswith('#'):
        if current_section != "":
            output_html += "            </div>\n        </div>\n"
        current_section = line[1:].strip()
        output_html += f"""
        <!-- {current_section} -->
        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem;">
            <h3 style="color: var(--gold); border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem; font-family: 'Crimson Text', serif; font-size: 1.25rem;">
                <i class="fas fa-archive" style="margin-right: 0.5rem; font-size: 1rem; color: var(--text-muted);"></i>
                {current_section}
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 0.75rem;">
"""
    else:
        title, link = line.split('|')
        output_html += f"""                <a href="{link}" target="_blank" style="display: flex; align-items: flex-start; gap: 0.75rem; text-decoration: none; padding: 0.75rem; background: rgba(255,255,255,0.02); border: 1px solid transparent; border-radius: 4px; transition: all 0.2s;">
                    <i class="fas fa-file-pdf" style="color: var(--text-muted); margin-top: 0.2rem;"></i>
                    <span style="color: var(--text); font-size: 0.8rem; line-height: 1.4;">{title}</span>
                </a>\n"""

if current_section != "":
    output_html += "            </div>\n        </div>\n"

output_html += "        </div>\n\n        <!-- About -->"

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the "<!-- About -->" token with the new HTML block
replaced = content.replace("<!-- About -->", output_html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(replaced)

print("Injected Zenodo library into index.html successfully.")
