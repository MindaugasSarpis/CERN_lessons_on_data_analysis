from graphviz import Digraph

dot = Digraph()

# Add nodes
dot.node('AI', 'Artificial Intelligence (AI)')
dot.node('ML', 'Machine Learning (ML)')
dot.node('NLP', 'Natural Language Processing (NLP)')
dot.node('CV', 'Computer Vision')
dot.node('AV', 'Autonomous Vehicles')
dot.node('Healthcare', 'Healthcare')
dot.node('Robotics', 'Robotics')
dot.node('SL', 'Supervised Learning')
dot.node('UL', 'Unsupervised Learning')
dot.node('RL', 'Reinforcement Learning')
dot.node('Reg', 'Regression')
dot.node('Class', 'Classification')
dot.node('SR', 'Speech Recognition')
dot.node('TG', 'Text Generation')
dot.node('CGPT', 'ChatGPT')
dot.node('SA', 'Sentiment Analysis')
dot.node('IC', 'Image Classification')
dot.node('OD', 'Object Detection')
dot.node('FR', 'Facial Recognition')
dot.node('MI', 'Medical Imaging')

# Add edges
dot.edge('AI', 'ML', 'Includes')
dot.edge('AI', 'NLP', 'Includes')
dot.edge('AI', 'CV', 'Includes')
dot.edge('AI', 'AV', 'Application')
dot.edge('AI', 'Healthcare', 'Application')
dot.edge('AI', 'Robotics', 'Application')
dot.edge('ML', 'SL', 'Subtype')
dot.edge('ML', 'UL', 'Subtype')
dot.edge('ML', 'RL', 'Subtype')
dot.edge('SL', 'Reg', 'Example')
dot.edge('SL', 'Class', 'Example')
dot.edge('NLP', 'SR', 'Includes')
dot.edge('NLP', 'TG', 'Includes')
dot.edge('NLP', 'CGPT', 'Example')
dot.edge('NLP', 'SA', 'Example')
dot.edge('CV', 'IC', 'Includes')
dot.edge('CV', 'OD', 'Includes')
dot.edge('CV', 'FR', 'Application')
dot.edge('CV', 'MI', 'Application')

# Render the graph
dot.render('ai_knowledge_graph', view=True)
