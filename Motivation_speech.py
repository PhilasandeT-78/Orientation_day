import streamlit as st

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Mathematical Sciences | Your Future",
    layout="wide"
)

# ---------------------------------
# SIDEBAR MENU
# ---------------------------------
st.sidebar.title("🎓 Mathematical Sciences")
menu = st.sidebar.radio(
    "Navigate",
    ["Welcome", "Motivational Message", "Career Paths", "Statistics Game","Probability Game 🎲"]
)


# ---------------------------------
# WELCOME PAGE
# ---------------------------------
if menu == "Welcome":
    st.title("Welcome to Mathematical Sciences")
    st.subheader("Your Journey Starts Here")

    st.markdown("""
    Mathematical Sciences is more than just numbers and equations.
    It is about **thinking**, **problem-solving**, and **building the future with data**.

    This platform is designed to:
    - Motivate you
    - Show you what is possible
    - Help you connect your studies to real careers
    """)

    st.success("💡 You are not here by accident. You belong here.")

# ---------------------------------
# MOTIVATIONAL MESSAGE
# ---------------------------------
elif menu == "Motivational Message":
    st.title("A Message to First-Year Students")

    st.markdown("""
    **Greetings everyone,**

    My name is **Philasande Tshusha**. I am a **Postgraduate Diploma student**
    in the **Mathematics and Physics Department**, and I also work as a
    **Junior Data Analyst** under the **FUNDANI CHED Department**.
     
    You sitting here means you are beginning your academic journey in the Diploma in Mathematical Science, a field that forms part of the backbone of science, Technology and data-driven decision-making.
    By choosing this qualification, you have committed yourselves to a discipline that demands critical thinking and perseverance
     
    Mathematical Science is more than a collection of formulas and computations. 
    It develops the ability to reason logically, analyse complex systems and to approach problems with clarity and structure.
    These skills are essential for a wide range of careers, particularly in the rapidly growing and data analytics space.
    
    As a first-year student, it is important to understand that this journey will not be always smooth. 
    You will encounter academic challenges, moments of uncertainty and periods of self-doubt. 
    These experiences are not indicators of failure, but rather important indicators of intellectual growth. 
    Always remember your journey is not the same as that of your peer, you are all coming from different backgrounds, you do not share the same goal and responsibilities, and you most certainly will not grasp academic content the same way.
    
    From my own academic and professional experience, I can confidently say that the foundations you will build here are invaluable. 
    The skills you acquire during this diploma will prepare you not only for further study, but also for meaningful participation in the modern workforce.
    
    Success in Mathematical Sciences does not rely solely on natural ability. 
    It is built through consistent effort, discipline, effective time management, and the willingness to seek support when needed. 
    Make use of the academic resources available to you, engage actively in your learning, and collaborate with your peers.
    
    As you move forward, I encourage you to remain committed to your goals, to embrace challenges as opportunities for growth, and to believe in your capacity to succeed.
    I wish you a productive and successful academic year and every success in your studies within Mathematical Sciences.

    Welcome to Mathematical Sciences.
    Welcome to your future.
    """)
 
elif menu == "Career Paths":
    st.title("Career Paths in Mathematical Sciences")
    st.write("Explore some of the exciting careers you can pursue.")

    careers = [
        {
            "title": "Statistician",
            "image": "https://tse2.mm.bing.net/th/id/OIP.RxjZBolGPyVa2sRn1TWVjwHaEK?rs=1&pid=ImgDetMain&o=7&rm=3",
            "description": "Works with data to design studies, analyze results, and support decision-making.",
            "skills": "Probability, statistical inference, data analysis",
            "tools": "R, Python, SPSS, SAS"
        },
        {
            "title": "Mathematician",
            "image": "https://th.bing.com/th/id/OIP.VJ3P3qYq2bjpXLuybsgmtgHaFF?w=237&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "description": "Develops mathematical models to solve theoretical and real-world problems.",
            "skills": "Abstract thinking, modelling, proofs",
            "tools": "MATLAB, Mathematica, Python"
        },
        {
            "title": "Data Analyst",
            "image": "https://th.bing.com/th/id/OIP.3L_ayP3Io6qtkqYgtxRo9QHaDt?w=312&h=175&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "description": "Transforms raw data into insights that support business and research decisions.",
            "skills": "Data cleaning, visualization, communication",
            "tools": "Excel, SQL, Python, Power BI"
        },
        {
            "title": "Data Engineer",
            "image": "https://th.bing.com/th/id/OIP.M7bn2d1smKQoHEOQHWOf7wHaHa?w=174&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "description": "Builds and maintains data pipelines and databases for analytics and AI.",
            "skills": "Databases, programming, systems thinking",
            "tools": "SQL, Python, Spark, Cloud platforms"
        },
        {
            "title": "Machine Learning Engineer",
            "image": "https://th.bing.com/th/id/OIP.B9HkHRem-rPttyGmLKbsoQHaD6?w=293&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "description": "Designs and deploys machine learning models in real-world systems.",
            "skills": "Machine learning, algorithms, software engineering",
            "tools": "Python, TensorFlow, PyTorch"
        },
        {
            "title": "Data Scientist",
            "image": "https://th.bing.com/th/id/OIP.w50thsSvTmYKpeHT5vrHWQHaEK?w=308&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "description": "Uses statistics, programming, and machine learning to solve complex problems.",
            "skills": "Statistics, programming, critical thinking",
            "tools": "Python, R, SQL, Jupyter"
        },
        {
            "title": "BI Analyst",
            "image": "https://th.bing.com/th/id/OIP.H91cR-AE7qaJp2ehdx2sNQHaFj?w=220&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            "description": "Focuses on dashboards and reporting to support strategic decisions.",
            "skills": "Business understanding, visualization",
            "tools": "Power BI, Tableau, SQL, Excel"
        }
    ]

    for career in careers:
        st.markdown("---")
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(career["image"], use_container_width=True)

        with col2:
            st.subheader(career["title"])
            st.write(career["description"])
            st.markdown(f"**Key Skills:** {career['skills']}")
            st.markdown(f"**Common Tools:** {career['tools']}")

elif menu == "Statistics Game":
    import random
    import statistics
    import matplotlib.pyplot as plt

    st.title("🎯 Guess the Average")
    st.write("Estimate the **mean** and **median**, then explore the data visually.")

    # -----------------------------
    # RANDOM DATASET GENERATOR
    # -----------------------------
    if "data" not in st.session_state:
        st.session_state.data = []

    if st.button("🎲 Generate New Dataset"):
        st.session_state.data = sorted(
            [random.randint(40, 95) for _ in range(12)]
        )

    if st.session_state.data:
        data = st.session_state.data

        st.markdown("### 📊 Dataset (Test Marks)")
        st.write(data)

        # -----------------------------
        # USER GUESSES
        # -----------------------------
        mean_guess = st.number_input(
            "Your guess for the MEAN",
            min_value=0.0,
            max_value=100.0,
            step=0.5
        )

        median_guess = st.number_input(
            "Your guess for the MEDIAN",
            min_value=0.0,
            max_value=100.0,
            step=0.5
        )

        if st.button("✅ Check Answers"):
            mean_actual = statistics.mean(data)
            median_actual = statistics.median(data)

            st.success(f"Correct Mean: {mean_actual:.2f}")
            st.success(f"Correct Median: {median_actual:.2f}")

            # -----------------------------
            # HISTOGRAM
            # -----------------------------
            fig, ax = plt.subplots()
            ax.hist(data, bins=6)
            ax.axvline(mean_actual, linestyle="--", label="Mean")
            ax.axvline(median_actual, linestyle=":", label="Median")
            ax.set_title("Distribution of Test Marks")
            ax.set_xlabel("Marks")
            ax.set_ylabel("Frequency")
            ax.legend()

            st.pyplot(fig)

            # -----------------------------
            # LEARNING INSIGHT
            # -----------------------------
            st.info("""
            📌 **Statistical Insight**
            - The **mean** is sensitive to extreme values.
            - The **median** represents the middle of the data.
            - The histogram shows whether the data is symmetric or skewed.
            """)

    else:
        st.warning("Click 🎲 **Generate New Dataset** to start the game.")




elif menu == "Probability Game 🎲":
    import random
    import matplotlib.pyplot as plt

    st.title("🎲 Coin & Dice Probability Simulator")

    game_type = st.radio(
        "Choose a simulation:",
        ["Coin Toss", "Dice Roll"]
    )

    trials = st.slider("Number of simulations:", 10, 5000, 100)

    if st.button("Run Simulation"):
        
        # -----------------------------------
        # COIN TOSS
        # -----------------------------------
        if game_type == "Coin Toss":
            results = [random.choice(["Heads", "Tails"]) for _ in range(trials)]
            heads_count = results.count("Heads")
            tails_count = results.count("Tails")

            st.subheader("Results")
            st.write(f"Heads: {heads_count}")
            st.write(f"Tails: {tails_count}")

            experimental_prob = heads_count / trials
            st.success(f"Experimental P(Heads) = {experimental_prob:.4f}")
            st.info("Theoretical P(Heads) = 0.5")

            # Plot
            fig, ax = plt.subplots()
            ax.bar(["Heads", "Tails"], [heads_count, tails_count])
            ax.set_title("Coin Toss Outcomes")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

        # -----------------------------------
        # DICE ROLL
        # -----------------------------------
        else:
            results = [random.randint(1, 6) for _ in range(trials)]
            counts = [results.count(i) for i in range(1, 7)]

            st.subheader("Results")
            for i in range(6):
                st.write(f"Face {i+1}: {counts[i]}")

            experimental_prob = counts[0] / trials
            st.success(f"Experimental P(1) = {experimental_prob:.4f}")
            st.info("Theoretical P(1) = 1/6 ≈ 0.1667")

            # Plot
            fig, ax = plt.subplots()
            ax.bar(range(1, 7), counts)
            ax.set_title("Dice Roll Outcomes")
            ax.set_xlabel("Dice Face")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

        # -----------------------------------
        # LEARNING INSIGHT
        # -----------------------------------
        st.markdown("---")
        st.info("""
        📌 **Law of Large Numbers**
        As the number of simulations increases,
        the experimental probability approaches the theoretical probability.
        Try increasing the number of simulations and observe what happens!
        """)

  

  

