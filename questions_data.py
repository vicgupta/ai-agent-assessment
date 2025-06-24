assessment_data = {
    "categories": [
        {"id": 0, "name": "Welcome", "description": "Introduction to the assessment", "question_range": []},
        {"id": 1, "name": "Agentic Vision & Strategy", "description": "How clearly is the organization defining its vision for AI agents, and how well are these agent initiatives aligned with overall business goals and digital transformation efforts? This category assesses the strategic foresight and planning around autonomous and intelligent agents.", "question_range": [1, 5]},
        {"id": 2, "name": "Agent Architecture & Infrastructure", "description": "This category evaluates the underlying technical foundation required to build, deploy, and scale AI agents. It covers everything from computational resources and specialized platforms to connectivity, modularity, and the ability to integrate agents into existing systems.", "question_range": [6, 10]},
        {"id": 3, "name": "Data for Agents", "description": "Beyond general data quality, this focuses on the availability, quality, and governance of data specifically needed for agent learning, decision-making, and operational feedback. This includes real-time data streams, context-rich data, and data for training agent behaviors.", "question_range": [11, 15]},
        {"id": 4, "name": "Agentic Intelligence & Autonomy", "description": "This assesses the sophistication of the agents themselves—their ability to perceive, reason, plan, learn, and act independently. It covers levels of autonomy, complex problem-solving capabilities, and adaptation in dynamic environments.", "question_range": [16, 20]},
        {"id": 5, "name": "Human-Agent Teaming & Oversight", "description": "This crucial category examines how humans and agents collaborate. It assesses the mechanisms for human supervision, intervention, trust calibration, and the clarity of human-agent interaction models (e.g., human-in-the-loop, human-on-the-loop).", "question_range": [21, 25]},
        {"id": 6, "name": "Agent Development & MLOps", "description": "This focuses on the processes and tools used to develop, test, deploy, monitor, and maintain AI agents throughout their lifecycle. It includes continuous integration/continuous deployment (CI/CD) for agents, versioning, performance monitoring, and rapid iteration.", "question_range": [26, 30]},
        {"id": 7, "name": "Agent Security & Resilience", "description": "Given their autonomy and potential impact, agents require specialized security considerations. This category evaluates measures to protect agents from adversarial attacks, ensure their robustness against failures, and prevent unintended or malicious behaviors.", "question_range": [31, 35]},
        {"id": 8, "name": "Agent Operations & Performance", "description": "This is about the day-to-day operational effectiveness of deployed agents. It assesses their efficiency, reliability, scalability, and ability to handle incidents. It also looks at the processes for continuous performance optimization and resource management.", "question_range": [36, 40]},
        {"id": 9, "name": "Agent Ethics & Accountability", "description": "This addresses the critical ethical dimensions of deploying autonomous agents. It assesses the frameworks for managing bias, ensuring fairness, maintaining transparency, and establishing clear lines of accountability for agent decisions and actions. This includes adherence to responsible AI principles.", "question_range": [41, 45]},
        {"id": 10, "name": "Regulatory Compliance for Agents", "description": "As agents become more sophisticated, they introduce new regulatory challenges. This category evaluates the organization's approach to complying with existing and emerging regulations related to autonomous systems, data privacy (especially with agent interactions), and industry-specific guidelines.", "question_range": [46, 50]}
    ],
    "questions": {
        # Category 1: Agentic Vision & Strategy (Q1-Q5)
        "q1": {
            "title": "1. AI Agent Vision & Strategic Alignment",
            "options": [
                {"value": 1, "label": "No defined vision or strategy for AI agents; initiatives are ad-hoc."},
                {"value": 2, "label": "Basic discussions on AI agents, but no clear alignment with business strategy."},
                {"value": 3, "label": "Clear vision for AI agents with defined objectives, partially aligned with business goals."},
                {"value": 4, "label": "AI agent strategy is integrated into enterprise business strategy and regularly updated to drive specific outcomes."},
                {"value": 5, "label": "AI agent vision drives significant business transformation and creates competitive differentiation across the organization."}
            ]
        },
        "q2": {
            "title": "2. Executive Sponsorship & Leadership for Agents",
            "options": [
                {"value": 1, "label": "Limited executive awareness or support for AI agent initiatives."},
                {"value": 2, "label": "Some executive interest in agents, but no dedicated leadership or champion."},
                {"value": 3, "label": "Appointed AI agent champion or committee with executive-level sponsorship."},
                {"value": 4, "label": "Dedicated C-level leadership (e.g., Chief AI Officer) with explicit responsibility for AI agents."},
                {"value": 5, "label": "AI agent leadership is a core component of all C-suite strategic decisions and resource allocation."}
            ]
        },
        "q3": {
            "title": "3. Identified Agent Use Cases & Value Proposition",
            "options": [
                {"value": 1, "label": "No clear identification of specific business problems AI agents can solve."},
                {"value": 2, "label": "Exploration of a few isolated, basic use cases for AI agents."},
                {"value": 3, "label": "Defined business cases for specific AI agent applications with measurable success metrics."},
                {"value": 4, "label": "A portfolio of high-value AI agent use cases with clear ROI models and demonstrated impact across functions."},
                {"value": 5, "label": "AI agents are central to core business processes, driving new value streams and fundamentally transforming operations."}
            ]
        },
        "q4": {
            "title": "4. Resource Allocation & Budget for Agents",
            "options": [
                {"value": 1, "label": "No dedicated budget or resources for AI agent initiatives."},
                {"value": 2, "label": "Ad-hoc, project-specific funding for basic agent pilots."},
                {"value": 3, "label": "Allocated budget and resources for structured AI agent programs and foundational capabilities."},
                {"value": 4, "label": "Strategic investment in AI agents as a key technology, with clear budget lines and resource planning."},
                {"value": 5, "label": "Significant, continuous investment in AI agent R&D, talent, and infrastructure, viewed as a strategic imperative."}
            ]
        },
        "q5": {
            "title": "5. Organizational Readiness for Agent Adoption",
            "options": [
                {"value": 1, "label": "High resistance to change; fear of AI agents replacing jobs."},
                {"value": 2, "label": "Cautious acceptance; some skepticism about agent benefits."},
                {"value": 3, "label": "Openness to AI agent adoption with active communication and engagement."},
                {"value": 4, "label": "Enthusiastic adoption of agents with a culture of experimentation and innovation."},
                {"value": 5, "label": "An 'agent-first' mindset with employees actively driving and embracing agent innovation and transformation."}
            ]
        },
        # Category 2: Agent Architecture & Infrastructure (Q6-Q10)
        "q6": {
            "title": "6. Scalable Computing for Agents",
            "options": [
                {"value": 1, "label": "Limited computing resources, primarily on-premise, unsuitable for agent workloads."},
                {"value": 2, "label": "Basic cloud setup or isolated on-premise clusters with some capacity for small agent pilots."},
                {"value": 3, "label": "Hybrid cloud environment with dedicated, scalable compute resources (e.g., GPUs) for AI agent training and inference."},
                {"value": 4, "label": "Cloud-native architecture with elastic auto-scaling capabilities optimized for diverse AI agent workloads."},
                {"value": 5, "label": "Dynamic, distributed computing fabric (edge-to-cloud) capable of supporting complex, real-time AI agent ecosystems."}
            ]
        },
        "q7": {
            "title": "7. Agent Platform & Tooling",
            "options": [
                {"value": 1, "label": "No dedicated platforms or specialized tools for building or managing AI agents."},
                {"value": 2, "label": "Ad-hoc use of basic ML libraries and open-source components for agent development."},
                {"value": 3, "label": "Integrated AI/ML platform supporting core agent development, simulation, and basic deployment."},
                {"value": 4, "label": "Enterprise-grade AI agent platform with advanced features for multi-agent system design, orchestration, and lifecycle management."},
                {"value": 5, "label": "A bespoke, highly optimized agent development and management platform, leveraging cutting-edge research and proprietary tools."}
            ]
        },
        "q8": {
            "title": "8. Agent Integration & Interoperability",
            "options": [
                {"value": 1, "label": "Siloed legacy systems with significant manual effort to integrate agents."},
                {"value": 2, "label": "Some API development for basic agent integration, often point-to-point."},
                {"value": 3, "label": "Standardized API gateways and microservices architecture facilitating AI agent integration across key systems."},
                {"value": 4, "label": "An API-first architecture with a comprehensive service mesh enabling seamless, secure agent communication and data exchange."},
                {"value": 5, "label": "An event-driven, distributed architecture where AI agents can autonomously discover and interact with any required service or data source."}
            ]
        },
        "q9": {
            "title": "9. Agent Environment & Simulation Capabilities",
            "options": [
                {"value": 1, "label": "No specific environment or simulation tools for testing agent behavior."},
                {"value": 2, "label": "Basic sandboxes for isolated testing of individual agent components."},
                {"value": 3, "label": "Dedicated simulation environments for testing agent interactions and emergent behaviors in controlled scenarios."},
                {"value": 4, "label": "High-fidelity simulation platforms capable of mimicking complex real-world environments for robust agent training and validation."},
                {"value": 5, "label": "Continuous, adaptive simulation environments that integrate real-world data and feedback loops for ongoing agent optimization and safety validation."}
            ]
        },
        "q10": {
            "title": "10. Scalability of Agent Deployments",
            "options": [
                {"value": 1, "label": "Only capable of deploying a few, isolated AI agents with limited concurrency."},
                {"value": 2, "label": "Can deploy a small number of agents, but scaling beyond prototypes is challenging and manual."},
                {"value": 3, "label": "Infrastructure supports scaling of agent instances for defined use cases, with some automation."},
                {"value": 4, "label": "Robust orchestration (e.g., Kubernetes) for dynamic scaling and management of numerous AI agents in production."},
                {"value": 5, "label": "Cloud-agnostic, infinitely scalable architecture supporting large-scale, enterprise-wide AI agent deployments with autonomous resource management."}
            ]
        },
        # Category 3: Data for Agents (Q11-Q15)
        "q11": {
            "title": "11. Data Accessibility & Integration for Agents",
            "options": [
                {"value": 1, "label": "Data is fragmented and largely inaccessible for agent use; manual extraction required."},
                {"value": 2, "label": "Some centralized data stores, but agents struggle with data discovery and integration."},
                {"value": 3, "label": "Well-defined data pipelines and APIs enable agents to access structured data efficiently."},
                {"value": 4, "label": "Comprehensive data lake/fabric ensures agents can access diverse structured and unstructured data sources via automated processes."},
                {"value": 5, "label": "Real-time, intelligent data fabric with AI-driven discovery, semantic understanding, and autonomous provisioning of data for agents."}
            ]
        },
        "q12": {
            "title": "12. Real-time Data Processing for Agents",
            "options": [
                {"value": 1, "label": "Primarily batch processing; agents cannot react to real-time events."},
                {"value": 2, "label": "Near real-time data for some critical agent functions, with noticeable latency."},
                {"value": 3, "label": "Stream processing capabilities enable agents to act on real-time data for defined use cases."},
                {"value": 4, "label": "Comprehensive real-time data platform with event-driven architecture supporting complex agent reactive behaviors."},
                {"value": 5, "label": "Ultra-low latency data processing and edge computing infrastructure empowering agents with instantaneous situational awareness and action."}
            ]
        },
        "q13": {
            "title": "13. Contextual Data & Knowledge Representation for Agents",
            "options": [
                {"value": 1, "label": "Agents operate with minimal context; relying only on immediate inputs."},
                {"value": 2, "label": "Agents can retrieve basic historical data or static knowledge bases."},
                {"value": 3, "label": "Agents utilize integrated knowledge graphs or contextual data stores to enrich their understanding and decision-making."},
                {"value": 4, "label": "Agents build and refine dynamic, contextual knowledge models from various sources for nuanced decision-making."},
                {"value": 5, "label": "Autonomous agents continuously learn, update, and leverage sophisticated, evolving contextual knowledge bases for highly adaptive and intelligent behavior."}
            ]
        },
        "q14": {
            "title": "14. Data Governance for Agent Use",
            "options": [
                {"value": 1, "label": "No specific data governance policies for AI agents; unmanaged data access."},
                {"value": 2, "label": "Basic data access controls for agents, but no systematic governance for agent data usage."},
                {"value": 3, "label": "Formal data governance framework includes policies for agent data access, usage, and retention."},
                {"value": 4, "label": "Automated data governance tools enforce policies for agent data consumption, ensuring data quality and compliance at scale."},
                {"value": 5, "label": "Adaptive, AI-driven data governance proactively manages data for agents, ensuring optimal quality, compliance, and ethical use across all agent interactions."}
            ]
        },
        "q15": {
            "title": "15. Data Quality & Integrity for Agent Learning",
            "options": [
                {"value": 1, "label": "Poor data quality for agent training; frequent errors and inconsistencies."},
                {"value": 2, "label": "Moderate data quality; requires significant manual cleaning for agent use."},
                {"value": 3, "label": "Established data quality processes ensure reliable data for agent training and operation."},
                {"value": 4, "label": "Automated data validation and cleansing pipelines maintain high data quality for all agent-related data."},
                {"value": 5, "label": "Self-healing data systems and AI-driven quality checks ensure exceptional data integrity, continuously optimizing data for agent learning."}
            ]
        },
        # Category 4: Agentic Intelligence & Autonomy (Q16-Q20)
        "q16": {
            "title": "16. Goal-Driven Behavior & Planning",
            "options": [
                {"value": 1, "label": "Agents are purely reactive; no goal-setting or planning capabilities."},
                {"value": 2, "label": "Agents execute predefined scripts or simple sequential tasks without dynamic planning."},
                {"value": 3, "label": "Agents can define sub-goals and execute multi-step plans to achieve a higher-level objective."},
                {"value": 4, "label": "Agents autonomously adapt and optimize their plans based on real-time environmental feedback and unexpected events."},
                {"value": 5, "label": "Agents exhibit sophisticated goal reasoning, dynamic replanning, and can infer implicit goals to optimize complex outcomes."}
            ]
        },
        "q17": {
            "title": "17. Learning & Adaptation Capabilities of Agents",
            "options": [
                {"value": 1, "label": "Agents have fixed behaviors; no learning or adaptation post-deployment."},
                {"value": 2, "label": "Agents can be manually retrained or updated based on performance issues."},
                {"value": 3, "label": "Agents can learn from new data inputs, improving performance within predefined parameters."},
                {"value": 4, "label": "Agents exhibit continuous learning from interactions and environmental feedback, leading to autonomous behavioral improvements."},
                {"value": 5, "label": "Agents are self-improving, capable of active experimentation, discovering novel strategies, and adapting to entirely new situations without explicit reprogramming."}
            ]
        },
        "q18": {
            "title": "18. Decision-Making Under Uncertainty",
            "options": [
                {"value": 1, "label": "Agents fail or halt when encountering unexpected or uncertain situations."},
                {"value": 2, "label": "Agents require human intervention or fallback to default rules in uncertain scenarios."},
                {"value": 3, "label": "Agents can make decisions under moderate uncertainty using probabilistic reasoning or predefined contingencies."},
                {"value": 4, "label": "Agents leverage advanced probabilistic models and reinforcement learning to make optimal decisions in highly uncertain and dynamic environments."},
                {"value": 5, "label": "Agents possess robust metacognitive abilities, capable of assessing their own uncertainty, requesting clarification, and strategically exploring options in novel, ambiguous situations."}
            ]
        },
        "q19": {
            "title": "19. Tool Use & External Interaction",
            "options": [
                {"value": 1, "label": "Agents are isolated, with no ability to use external tools or systems."},
                {"value": 2, "label": "Agents can call a very limited set of pre-configured internal APIs/tools."},
                {"value": 3, "label": "Agents can dynamically select and utilize a range of internal tools and APIs to accomplish tasks."},
                {"value": 4, "label": "Agents can integrate with and expertly utilize a broad ecosystem of both internal and external (e.g., third-party) tools and APIs."},
                {"value": 5, "label": "Agents demonstrate advanced tool creation and adaptation, dynamically learning to use new tools or combine existing ones in novel ways to achieve complex goals."}
            ]
        },
        "q20": {
            "title": "20. Multi-Agent Coordination & Collaboration",
            "options": [
                {"value": 1, "label": "Agents operate independently; no coordination or communication."},
                {"value": 2, "label": "Limited, pre-programmed communication between a few agents for simple task handoffs."},
                {"value": 3, "label": "Agents can coordinate activities and share information through established communication protocols to achieve shared goals."},
                {"value": 4, "label": "Agents dynamically form teams, negotiate tasks, and collaboratively solve complex problems across a distributed environment."},
                {"value": 5, "label": "Sophisticated multi-agent systems with emergent collective intelligence, autonomously optimizing resource allocation and achieving super-human level collaboration."}
            ]
        },
        # Category 5: Human-Agent Teaming & Oversight (Q21-Q25)
        "q21": {
            "title": "21. Transparency & Explainability of Agent Decisions",
            "options": [
                {"value": 1, "label": "Agent decisions are black-box; reasons for actions are not accessible to humans."},
                {"value": 2, "label": "Basic logging of agent actions is available, but the reasoning process is unclear or requires technical interpretation."},
                {"value": 3, "label": "Agents provide some level of explainability for their decisions (e.g., highlighting key inputs or rules used), allowing human review."},
                {"value": 4, "label": "Agents offer clear, interpretable explanations for their actions and can justify their choices in human-understandable terms."},
                {"value": 5, "label": "Agents engage in natural language explanations, allowing for dynamic queries and deep understanding of their reasoning, even for complex multi-step tasks or emergent behaviors."}
            ]
        },
        "q22": {
            "title": "22. Human-in-the-Loop (HIL) & Human-on-the-Loop (HOL) Mechanisms",
            "options": [
                {"value": 1, "label": "No formal human oversight mechanisms for agent operations; full automation or manual control."},
                {"value": 2, "label": "Manual intervention is required for all critical agent decisions or errors, leading to bottlenecks."},
                {"value": 3, "label": "Clear processes exist for human review and approval of agent-generated plans or high-risk actions before execution."},
                {"value": 4, "label": "Sophisticated Human-on-the-Loop (HOL) systems are in place, where humans monitor agent performance and intervene only when necessary, with clear triggers."},
                {"value": 5, "label": "Adaptive HIL/HOL frameworks dynamically adjust human involvement based on agent confidence, risk assessment, and contextual factors, optimizing for efficiency, safety, and continuous learning."}
            ]
        },
        "q23": {
            "title": "23. Human-Agent Trust & Calibration",
            "options": [
                {"value": 1, "label": "Humans distrust agents and are hesitant to delegate tasks, leading to underutilization."},
                {"value": 2, "label": "Trust is built on a case-by-case basis, with frequent human verification required for agent outputs."},
                {"value": 3, "label": "Humans generally trust agents for routine tasks, with established oversight mechanisms to build confidence."},
                {"value": 4, "label": "Humans and agents effectively calibrate their trust levels, understanding each other's strengths, limitations, and failure modes."},
                {"value": 5, "label": "Trust is high and dynamically calibrated, with humans and agents seamlessly adapting roles based on real-time performance, context, and shared understanding of intent."}
            ]
        },
        "q24": {
            "title": "24. Shared Mental Models & Collaboration Tools",
            "options": [
                {"value": 1, "label": "Humans and agents operate with disconnected understanding of tasks and goals; no shared interface."},
                {"value": 2, "label": "Basic dashboards show agent status, but no shared view of ongoing work or agent reasoning."},
                {"value": 3, "label": "Collaboration tools provide a common interface for humans and agents to track progress and share basic information."},
                {"value": 4, "label": "Sophisticated shared mental models are facilitated by tools that enable humans to understand agent intent, and agents to interpret human instructions and goals effectively."},
                {"value": 5, "label": "Collaborative platforms seamlessly blend human and agent workflows, with AI supporting human cognitive processes and vice-versa, fostering true human-agent teaming and shared awareness."}
            ]
        },
        "q25": {
            "title": "25. Agent Feedback & Continuous Improvement Integration",
            "options": [
                {"value": 1, "label": "Human feedback on agent performance is not systematically captured or used for improvement."},
                {"value": 2, "label": "Ad-hoc human feedback is provided, leading to occasional manual adjustments to agent rules or models."},
                {"value": 3, "label": "Structured mechanisms exist for humans to provide feedback, which is used for agent retraining or refinement in a semi-automated way."},
                {"value": 4, "label": "Agents actively solicit clear feedback from human users and seamlessly integrate it into their learning processes to improve performance."},
                {"value": 5, "label": "A continuous, closed-loop feedback system is established, where human insights drive autonomous agent self-improvement and adaptation in real-time, fostering a symbiotic learning relationship."}
            ]
        },
        # Category 6: Agent Development & MLOps (Q26-Q30)
        "q26": {
            "title": "26. Agent Development Methodologies",
            "options": [
                {"value": 1, "label": "No formal methodology; agent development is unstructured and experimental."},
                {"value": 2, "label": "Ad-hoc scripting or basic waterfall approach for agent development."},
                {"value": 3, "label": "Agile or iterative methodologies applied to agent development, with defined sprints and feedback loops."},
                {"value": 4, "label": "Specialized agent development methodologies (e.g., goal-oriented, multi-agent system design patterns) are consistently applied."},
                {"value": 5, "label": "Leading-edge, adaptable methodologies that enable rapid prototyping, experimentation, and robust engineering of complex AI agent systems."}
            ]
        },
        "q27": {
            "title": "27. CI/CD & Automated Deployment for Agents",
            "options": [
                {"value": 1, "label": "Manual deployment processes; no automation for agent releases."},
                {"value": 2, "label": "Basic scripting for agent deployment, but lack of continuous integration or delivery."},
                {"value": 3, "label": "Established CI/CD pipelines automate building, testing, and deployment of individual AI agent components."},
                {"value": 4, "label": "Comprehensive MLOps pipelines with automated testing, versioning, and staged deployment for complex multi-agent systems."},
                {"value": 5, "label": "Fully automated, self-healing CI/CD for agents, supporting autonomous deployment, A/B testing, and intelligent rollback based on performance metrics."}
            ]
        },
        "q28": {
            "title": "28. Agent Model & Code Versioning",
            "options": [
                {"value": 1, "label": "No systematic versioning for agent code, models, or configurations."},
                {"value": 2, "label": "Basic source code control; models and configurations are managed inconsistently."},
                {"value": 3, "label": "Centralized version control for all agent assets (code, models, data, configurations) enabling reproducibility."},
                {"value": 4, "label": "Automated versioning and lineage tracking for every component of the agent system, ensuring auditability and traceability."},
                {"value": 5, "label": "Intelligent version management systems that automatically track, compare, and recommend optimal agent versions based on performance, cost, and ethical metrics."}
            ]
        },
        "q29": {
            "title": "29. Agent Testing & Validation",
            "options": [
                {"value": 1, "label": "No structured testing for agent behavior; relying on manual observation."},
                {"value": 2, "label": "Basic unit tests for agent code; limited functional testing of agent actions."},
                {"value": 3, "label": "Automated functional, integration, and performance testing for agents within controlled environments."},
                {"value": 4, "label": "Comprehensive testing frameworks including adversarial testing, robustness testing, and behavior-driven development for agents."},
                {"value": 5, "label": "AI-driven testing and validation for agents, continuously generating test cases, identifying edge cases, and self-correcting through simulations and real-world feedback."}
            ]
        },
        "q30": {
            "title": "30. Infrastructure as Code (IaC) for Agents",
            "options": [
                {"value": 1, "label": "Manual provisioning of infrastructure for agent deployments."},
                {"value": 2, "label": "Some scripts for infrastructure setup; inconsistent environments."},
                {"value": 3, "label": "IaC used for basic infrastructure components supporting agents, ensuring reproducibility."},
                {"value": 4, "label": "Full IaC implementation for all agent-related infrastructure, enabling immutable deployments and environment consistency."},
                {"value": 5, "label": "Dynamic, self-provisioning infrastructure managed entirely as code, with autonomous optimization for agent workloads and rapid environment spin-up/down."}
            ]
        },
        # Category 7: Agent Security & Resilience (Q31-Q35)
        "q31": {
            "title": "31. Agent Specific Threat Modeling & Risk Assessment",
            "options": [
                {"value": 1, "label": "No specific threat modeling for AI agents; standard IT security only."},
                {"value": 2, "label": "Basic awareness of new threats from agents, but no formal assessment."},
                {"value": 3, "label": "Formal threat modeling and risk assessment processes specifically for AI agents, including adversarial attacks."},
                {"value": 4, "label": "Proactive and continuous threat modeling integrated into the agent development lifecycle, addressing novel attack vectors."},
                {"value": 5, "label": "Predictive threat intelligence for AI agents, anticipating and mitigating emerging threats before they materialize, with adaptive defense mechanisms."}
            ]
        },
        "q32": {
            "title": "32. Data Security & Privacy for Agent Interactions",
            "options": [
                {"value": 1, "label": "Limited data security for agents; potential for data leakage during interactions."},
                {"value": 2, "label": "Basic encryption and access controls for agent-processed data."},
                {"value": 3, "label": "Comprehensive data encryption (at rest and in transit) and fine-grained access control for all data used by agents."},
                {"value": 4, "label": "Implementation of advanced privacy-enhancing technologies (PETs) like differential privacy or federated learning for sensitive agent data."},
                {"value": 5, "label": "End-to-end zero-trust data security architecture for agents, with continuous monitoring, immutable audit trails, and autonomous remediation of privacy breaches."}
            ]
        },
        "q33": {
            "title": "33. Agent Robustness to Adversarial Attacks",
            "options": [
                {"value": 1, "label": "No specific measures against adversarial attacks; agents are vulnerable."},
                {"value": 2, "label": "Basic awareness of adversarial attacks; some manual testing or basic filtering."},
                {"value": 3, "label": "Implementation of defensive techniques (e.g., adversarial training, input sanitization) to enhance agent robustness."},
                {"value": 4, "label": "Automated adversarial attack detection and real-time mitigation strategies for deployed agents."},
                {"value": 5, "label": "Self-healing and adaptive agents that proactively learn to defend against novel adversarial attacks and maintain integrity in hostile environments."}
            ]
        },
        "q34": {
            "title": "34. Agent Failure Modes & Safe Fallbacks",
            "options": [
                {"value": 1, "label": "Agent failures lead to system crashes or unsafe states; no graceful degradation."},
                {"value": 2, "label": "Agents report basic errors; often require manual intervention to recover."},
                {"value": 3, "label": "Defined safe fallback mechanisms and error handling routines for common agent failure modes."},
                {"value": 4, "label": "Automated self-recovery and graceful degradation mechanisms for agents, minimizing impact during failures."},
                {"value": 5, "label": "AI agents are designed for maximum resilience, autonomously identifying and recovering from complex failures, with built-in safety protocols that prioritize human safety and system integrity."}
            ]
        },
        "q35": {
            "title": "35. Protection Against Unintended Agent Behavior",
            "options": [
                {"value": 1, "label": "No mechanisms to prevent or detect unintended or emergent undesirable agent behaviors."},
                {"value": 2, "label": "Ad-hoc monitoring for obvious unintended behaviors; reactive adjustments."},
                {"value": 3, "label": "Behavioral constraints and guardrails are engineered into agent design to prevent unintended actions."},
                {"value": 4, "label": "Continuous monitoring of agent behavior for subtle deviations, with automated alerting and human-in-the-loop intervention for corrective action."},
                {"value": 5, "label": "Formal verification methods and AI-driven behavior auditing ensure agent actions strictly align with intended goals and ethical boundaries, proactively preventing unintended consequences."}
            ]
        },
        # Category 8: Agent Operations & Performance (Q36-Q40)
        "q36": {
            "title": "36. Agent Deployment & Rollout Management",
            "options": [
                {"value": 1, "label": "Ad-hoc, manual deployment of agents with no clear rollout strategy."},
                {"value": 2, "label": "Basic, often disruptive, deployment process for agent updates."},
                {"value": 3, "label": "Structured rollout plans (e.g., phased deployments, A/B testing) for new agent versions."},
                {"value": 4, "label": "Automated, low-risk deployment strategies (e.g., canary releases, blue/green deployments) for seamless agent updates."},
                {"value": 5, "label": "Dynamic, intelligent rollout management for agents, autonomously optimizing deployment based on real-time performance and user feedback."}
            ]
        },
        "q37": {
            "title": "37. Agent Performance Monitoring & Alerting",
            "options": [
                {"value": 1, "label": "Limited or no monitoring of agent operational performance."},
                {"value": 2, "label": "Basic metrics tracked for individual agents; manual review of performance data."},
                {"value": 3, "label": "Comprehensive monitoring of key agent performance indicators (KPIs) with automated alerting for thresholds."},
                {"value": 4, "label": "AI-driven anomaly detection for agent behavior, identifying subtle performance drifts or unexpected patterns."},
                {"value": 5, "label": "Predictive monitoring and self-diagnosis for agents, anticipating and preventing performance degradation, and autonomously optimizing configurations."}
            ]
        },
        "q38": {
            "title": "38. Resource Optimization for Agent Workloads",
            "options": [
                {"value": 1, "label": "Inefficient resource utilization; agents are over-provisioned or resource-starved."},
                {"value": 2, "label": "Manual, periodic adjustments to resources based on observed agent load."},
                {"value": 3, "label": "Basic auto-scaling of compute resources tied to agent demand."},
                {"value": 4, "label": "Dynamic resource allocation and cost optimization strategies for multi-agent workloads across heterogeneous environments."},
                {"value": 5, "label": "Autonomous resource management and cost optimization for all agent workloads, continuously adapting to fluctuating demands and maximizing efficiency."}
            ]
        },
        "q39": {
            "title": "39. Incident Response & Troubleshooting for Agents",
            "options": [
                {"value": 1, "label": "No formal incident response plan for agent failures; reactive and chaotic troubleshooting."},
                {"value": 2, "label": "Ad-hoc troubleshooting for agent incidents, often relying on individual expertise."},
                {"value": 3, "label": "Defined incident management protocols for agent failures, with clear escalation paths and basic diagnostics."},
                {"value": 4, "label": "Automated incident detection and diagnostic tools for agents, enabling rapid root cause analysis and assisted recovery."},
                {"value": 5, "label": "AI-driven incident management for agents, featuring autonomous problem diagnosis, self-healing capabilities, and continuous learning from past incidents."}
            ]
        },
        "q40": {
            "title": "40. Agent Performance Benchmarking & ROI Measurement",
            "options": [
                {"value": 1, "label": "No systematic measurement of AI agent business impact or performance against benchmarks."},
                {"value": 2, "label": "Basic KPIs tracked for some agent initiatives, often subjective."},
                {"value": 3, "label": "Comprehensive metrics framework with regular business impact assessment for agent deployments against predefined benchmarks."},
                {"value": 4, "label": "Advanced analytics linking AI agent investments directly to business outcomes, with continuous value optimization based on real-time performance data."},
                {"value": 5, "label": "Real-time, AI-driven business value measurement for agents, demonstrating clear ROI and enabling autonomous value optimization across the enterprise."}
            ]
        },
        # Category 9: Agent Ethics & Accountability (Q41-Q45)
        "q41": {
            "title": "41. Ethical AI Principles for Agents",
            "options": [
                {"value": 1, "label": "Limited awareness of ethical considerations specific to AI agents."},
                {"value": 2, "label": "Basic understanding of ethical concerns for agents, with informal discussions."},
                {"value": 3, "label": "Formal ethical AI framework specifically addresses design and deployment principles for agents (e.g., human oversight, beneficial intent)."},
                {"value": 4, "label": "Comprehensive ethical AI program with regular audits and stakeholder engagement focused on agent behavior and impact."},
                {"value": 5, "label": "Industry-leading responsible AI practices for agents, including transparent public commitments, continuous ethical review boards, and an 'ethics-by-design' approach."}
            ]
        },
        "q42": {
            "title": "42. Bias Detection & Mitigation in Agents",
            "options": [
                {"value": 1, "label": "No active consideration of bias in AI agent training or decision-making."},
                {"value": 2, "label": "Awareness of potential biases; ad-hoc checks for obvious issues in agent outputs."},
                {"value": 3, "label": "Formalized processes for identifying, measuring, and mitigating biases in agent data and algorithms."},
                {"value": 4, "label": "Quantitative metrics and automated tools are used for continuous bias detection and mitigation throughout the agent lifecycle."},
                {"value": 5, "label": "Proactive fairness-by-design approach for agents, with continuous monitoring, adaptive algorithms, and expert intervention to ensure equitable and inclusive outcomes."},
            ]
        },
        "q43": {
            "title": "43. Accountability for Agent Decisions & Actions",
            "options": [
                {"value": 1, "label": "Unclear lines of accountability for decisions made by autonomous agents."},
                {"value": 2, "label": "Accountability is informally assigned to individuals overseeing agent systems."},
                {"value": 3, "label": "Clear accountability matrix for agent decisions, outlining human roles and responsibilities."},
                {"value": 4, "label": "Robust audit trails and transparent logging mechanisms enable full traceability and accountability for all agent actions and their consequences."},
                {"value": 5, "label": "Legally sound and ethically robust accountability frameworks for agents, including mechanisms for dispute resolution and remediation of harmful outcomes, fostering public trust."}
            ]
        },
        "q44": {
            "title": "44. Explainability & Interpretability of Agent Actions",
            "options": [
                {"value": 1, "label": "Agent internal workings are opaque; decisions cannot be explained."},
                {"value": 2, "label": "Some attempts to log agent steps, but interpretation of reasoning is difficult for non-experts."},
                {"value": 3, "label": "Standardized methods for explaining agent decisions for key stakeholders, allowing for post-hoc analysis."},
                {"value": 4, "label": "Context-aware explainability tools provide insights into agent reasoning, enabling human understanding of complex behaviors."},
                {"value": 5, "label": "Proactive and interactive Explainable AI (XAI) systems for agents, continuously generating understandable rationales for all decisions and actions, fostering deep trust and debugging capabilities."}
            ]
        },
        "q45": {
            "title": "45. Societal & Environmental Impact Assessment of Agents",
            "options": [
                {"value": 1, "label": "No consideration of broader societal or environmental impacts of AI agent deployment."},
                {"value": 2, "label": "Basic awareness of potential negative impacts; no formal assessment process."},
                {"value": 3, "label": "Formalized impact assessment process for AI agents, considering ethical, social, and environmental consequences."},
                {"value": 4, "label": "Regular and comprehensive impact assessments integrated into agent development, with stakeholder engagement and mitigation strategies."},
                {"value": 5, "label": "Leading efforts in anticipatory governance for AI agents, actively shaping positive societal and environmental outcomes, and transparently addressing potential risks."}
            ]
        },
        # Category 10: Regulatory Compliance for Agents (Q46-Q50)
        "q46": {
            "title": "46. Awareness of Agent-Specific Regulations",
            "options": [
                {"value": 1, "label": "Limited to no awareness of emerging or existing regulations specific to autonomous AI agents."},
                {"value": 2, "label": "Basic awareness of some relevant regulations (e.g., GDPR), but not specifically for agents."},
                {"value": 3, "label": "Clear understanding of current and anticipated regulatory frameworks (e.g., EU AI Act, industry-specific agent regulations)."},
                {"value": 4, "label": "Proactive monitoring of global regulatory developments related to AI agents, with dedicated legal and compliance teams."},
                {"value": 5, "label": "Actively contributing to the shaping of AI agent policy and regulation, recognized as a leader in compliance best practices."}
            ]
        },
        "q47": {
            "title": "47. Compliance Framework for Agent Deployments",
            "options": [
                {"value": 1, "label": "No formal compliance framework for deploying AI agents."},
                {"value": 2, "label": "Ad-hoc compliance checks performed on agent projects, often post-deployment."},
                {"value": 3, "label": "Structured compliance framework integrated into the AI agent development and deployment lifecycle."},
                {"value": 4, "label": "Automated compliance monitoring and auditing tools for AI agents, ensuring continuous adherence to regulations."},
                {"value": 5, "label": "Predictive compliance systems for AI agents, autonomously identifying potential regulatory risks and recommending proactive adjustments to agent behavior or deployment."}
            ]
        },
        "q48": {
            "title": "48. Auditability & Traceability for Agent Actions",
            "options": [
                {"value": 1, "label": "Agent actions and decisions are not auditable or traceable."},
                {"value": 2, "label": "Basic logging exists, but it's difficult to reconstruct an agent's decision path for audit purposes."},
                {"value": 3, "label": "Detailed audit trails are maintained for all agent actions, inputs, and outputs, enabling post-hoc forensic analysis."},
                {"value": 4, "label": "Real-time, immutable audit logs and visualization tools provide complete traceability of agent behavior and decision-making for regulatory compliance."},
                {"value": 5, "label": "AI-enhanced auditability for agents, using AI itself to analyze audit trails for anomalies, ensure compliance, and generate comprehensive regulatory reports automatically."}
            ]
        },
        "q49": {
            "title": "49. Privacy & Data Protection for Agent Interactions",
            "options": [
                {"value": 1, "label": "Agent interactions with user data have not been specifically assessed for privacy risks."},
                {"value": 2, "label": "Basic data privacy measures applied to agents; some gaps in sensitive data handling."},
                {"value": 3, "label": "Privacy-by-design principles are applied to AI agent interactions, ensuring data minimization and secure processing."},
                {"value": 4, "label": "Advanced data protection mechanisms (e.g., homomorphic encryption, secure multi-party computation) are used for agents handling highly sensitive data."},
                {"value": 5, "label": "Leadership in data privacy for AI agents, with continuous privacy impact assessments, autonomous policy enforcement, and proactive adaptation to evolving privacy standards."}
            ]
        },
        "q50": {
            "title": "50. Cross-Border & Jurisdictional Compliance for Agents",
            "options": [
                {"value": 1, "label": "No consideration for cross-border regulatory implications of agents."},
                {"value": 2, "label": "Ad-hoc legal review for agent deployments in different jurisdictions."},
                {"value": 3, "label": "Legal and compliance teams provide guidance on cross-border implications for agent deployments."},
                {"value": 4, "label": "Centralized legal counsel and automated tools manage multi-jurisdictional compliance for global agent operations."},
                {"value": 5, "label": "Globally integrated compliance strategy for AI agents, with proactive legal intelligence, ensuring seamless and lawful operations across all international boundaries."}
            ]
        }
    },
    "maturity_levels": {
        1: {
            "title": "Level 1: Exploring",
            "description": "Your organization is in the early stages of AI agent exploration. Focus on building basic awareness, identifying foundational use cases, and establishing initial data and infrastructure practices to begin your agent journey.",
            "persona": "The 'Curious Novice' - This organization is dabbling, perhaps running a small, isolated pilot project. They are learning the basics and discovering what AI agents might be capable of, but lack a cohesive strategy or dedicated resources."
        },
        2: {
            "title": "Level 2: Experimenting",
            "description": "You're conducting AI agent pilots and building initial capabilities. Continue investing in foundational skills and architecture while carefully scaling successful experiments and establishing basic oversight.",
            "persona": "The 'Pilot Practitioner' - This organization has moved beyond simple curiosity. They are actively experimenting with a few agent projects, learning from successes and failures, and beginning to understand the technical and operational demands, but still lack broad adoption."
        },
        3: {
            "title": "Level 3: Implementing",
            "description": "You have structured AI agent initiatives with clear governance. Focus on integrating agents into core business units, developing robust operational practices, and establishing centers of excellence for agent development and deployment.",
            "persona": "The 'Structured Integrator' - This organization is strategically deploying AI agents in specific business functions. They have dedicated teams, established development and deployment processes, and are seeing tangible benefits, but agents are not yet pervasive across the entire enterprise."
        },
        4: {
            "title": "Level 4: Integrating",
            "description": "AI agents are becoming integral to your operations with strong governance, advanced capabilities, and effective human-agent teaming. Focus on scaling autonomous systems, leveraging agentic intelligence for competitive advantage, and proactive risk management.",
            "persona": "The 'Agent-Augmented Enterprise' - AI agents are a key part of how this organization operates. They are deeply integrated into workflows, augmenting human capabilities, and contributing significantly to strategic goals. Governance is robust, and proactive risk management is standard practice."
        },
        5: {
            "title": "Level 5: Innovating",
            "description": "You're an 'Agent-First' organization, setting industry standards in AI agent technology and responsible deployment. Continue pushing boundaries with advanced agentic intelligence, maintain leadership in ethical AI practices, and drive transformative business outcomes through autonomous agents.",
            "persona": "The 'Autonomous Pioneer' - This organization is at the forefront of AI agent innovation. Agents are not just integrated; they are driving new business models and capabilities. This organization is defining best practices, pushing technological boundaries, and leading the industry in responsible, advanced AI agent deployment."
        }
    },
    "scoring_logic": {
        "overall_score_calculation": "The overall maturity score is the average of the scores from all categories (excluding 'Welcome').",
        "category_score_calculation": "Each category's score is the average of the 'value' selected for its corresponding questions.",
        "score_to_maturity_level_mapping": [
            {"min_score": 1.0, "max_score": 1.99, "level_id": 1},
            {"min_score": 2.0, "max_score": 2.99, "level_id": 2},
            {"min_score": 3.0, "max_score": 3.99, "level_id": 3},
            {"min_score": 4.0, "max_score": 4.99, "level_id": 4},
            {"min_score": 5.0, "max_score": 5.0, "level_id": 5}
        ]
    }
}