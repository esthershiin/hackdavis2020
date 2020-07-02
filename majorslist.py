stri1 = '''African American Studies
American Studies
Ancient Egyptian Near Eastern Art Archaeology
Anthropology
Applied Mathematics
Architecture
Art History
Art Practice
Asian American Diaspora Studies
Asian Studies China
Asian Studies Japan
Asian Studies Multi Area
Astrophysics
Atmospheric Science
Bioengineering
Bioengineering Business Administration
Bioengineering Materials Science Engineering Joint Major
Business Administration
Celtic Studies
Chemical Biology
Chemical Engineering
Chemical Engineering Materials Science Joint Major
Chemical Engineering Nuclear Joint Major
Chemistry
Chicano Latino Studies
Chinese Language
Civil Engineering
Civil Engineering Business Administration
Classical Civilizations
Classical Languages
Cognitive Science
Comparative Literature
Computer Science
Conservation Resource Studies
Czech Polish Bosnian Croatian Serbian Language Literature
Dance Performance Studies
Data Science
Development Studies
Dutch Studies
East Asian Religion Thought Culture
Economics
Ecosystem Management Forestry
Electrical Engineering Computer Sciences
Electrical Engineering Computer Sciences Materials
Electrical Engineering Computer Sciences Nuclear Joint Major
Energy Engineering
Engineering Math Statistics
Engineering Physics
English
Environmental Earth Science
Environmental Economics Policy
Environmental Engineering Science
Environmental Sciences
Ethnic Studies
Film
Forestry Natural Resources
French
Gender Womens Studies
Genetics Plant Biology
Geography
Geology
Geophysics
German
Global Studies
Greek
History
Industrial Engineering Operations Research
Integrative Biology
Interdisciplinary Studies
Italian Studies
Japanese Language
Landscape Architecture
Latin
Latin American Studies
Legal Studies
Linguistics
Marine Science
Materials Science Engineering
Materials Science Engineering Mechanical Joint Major
Materials Science Engineering Nuclear Joint Major
Mathematics
Mechanical Engineering
Mechanical Engineering Business Administration
Mechanical Engineering Nuclear
Media Studies
Microbial Biology
Middle Eastern Studies
Molecular Environmental Biology
Molecular Cell Biology
Music
Native American Studies
Near Eastern Civilizations
Near Eastern Languages Literatures
Nuclear Engineering
Dietetics
Physiology And Metabolism
Nutritional Sciences Toxicology
Operations Research Management Science
Peace Conflict Studies
Philosophy
Physics
Planetary Science
Political Economy
Political Science
Premed
Prelaw
Psychology
Public Health
Rhetoric
Scandinavian
Slavic Languages Literatures
Social Welfare
Society Environment
Sociology
South Southeast Asian Studies
Spanish Portuguese
Statistics
Sustainable Environmental Design
Theater Performance Studies
Urban Studies'''

splitstring1 = stri1.split('\n')

stri2 = '''african-american-studies
american-studies
ancient-egyptian-near-eastern-art-archaeology
anthropology
applied-mathematics
architecture
art-history
art-practice
asian-american-diaspora-studies
asian-studies-china
asian-studies-japan
asian-studies-multi-area
astrophysics
atmospheric-science
bioengineering
bioengineering-business-administration
bioengineering-materials-science-engineering-joint-major
business-administration
celtic-studies
chemical-biology
chemical-engineering
chemical-engineering-materials-science-joint-major
chemical-engineering-nuclear-joint-major
chemistry
chicano-latino-studies
chinese-language
civil-engineering
civil-engineering-business-administration
classical-civilizations
classical-languages
cognitive-science
comparative-literature
computer-science
conservation-resource-studies
czech-polish-bosnian-croatian-serbian-language-literature
dance-performance-studies
data-science
development-studies
dutch-studies
east-asian-religion-thought-culture
economics
ecosystem-management-forestry
electrical-engineering-computer-sciences
electrical-engineering-computer-sciences-materials
electrical-engineering-computer-sciences-nuclear-joint-major
energy-engineering
engineering-math-statistics
engineering-physics
english
environmental-earth-science
environmental-economics-policy
environmental-engineering-science
environmental-sciences
ethnic-studies
film
forestry-natural-resources
french
gender-womens-studies
genetics-plant-biology
geography
geology
geophysics
german
global-studies
greek
history
industrial-engineering-operations-research
integrative-biology
interdisciplinary-studies
italian-studies
japanese-language
landscape-architecture
latin
latin-american-studies
legal-studies
linguistics
marine-science
materials-science-engineering
materials-science-engineering-mechanical-joint-major
materials-science-engineering-nuclear-joint-major
mathematics
mechanical-engineering
mechanical-engineering-business-administration
mechanical-engineering-nuclear
media-studies
microbial-biology
middle-eastern-studies
molecular-environmental-biology
molecular-cell-biology
music
native-american-studies
near-eastern-civilizations
near-eastern-languages-literatures
nuclear-engineering
dietetics
physiology-and-metabolism
nutritional-sciences-toxicology
operations-research-management-science
peace-conflict-studies
philosophy
physics
planetary-science
political-economy
political-science
premed
prelaw
psychology
public-health
rhetoric
scandinavian
slavic-languages-literatures
socialwelfare
society-environment
sociology
south-southeast-asian-studies
spanish-portuguese
statistics
sustainable-environmental-design
theater-performance-studies
urban-studies'''

splitstring2 = stri2.split('\n')

def full_list():
    total = []
    for i in range(len(splitstring1)):
        together = '<li><a href="./' + splitstring2[i] + '">' + splitstring1[i] + '</a></li>'
        total += [together]
    done = "\n".join(total)
    print(done)
