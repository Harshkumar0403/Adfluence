<!-- src/views/HomeView.vue -->
<template>
  <div class="home">
    <Navbar />
    <div class="content">
      <!-- Add any home page specific content here -->
      <div class="card" style="width: 18rem; margin-left:10px;border-radius:10px">
        <img class="card-img-top" src="https://www.adfluencehub.com/micro-influencer-package/assets/img/step3.svg" alt="Card image cap">
        <div class="card-body">
            <h4 style="color:#283618;font-family:Times-New-Roman"> <b>A Platform that helps you measure your CAMPAIGN'S TRUE INFLUENCE</b></h4>
            <p class="card-text" style="color:#e3d5ca">A full stack solution to manage end-to-end influencer campaigns at scale. Be it to tap into niched audiences through localized micro-influencers or a generic brand recognition campaign, our Influencer Marketing tool has it all sorted.
            </p>
        </div>
      </div>
      <div class="card" style="width: 18rem; margin-left:10px;border-radius:10px">
        <img class="card-img-top" src="https://www.adfluencehub.com/micro-influencer-package/assets/img/step1.svg" alt="Card image cap">
        <div class="card-body">
          <h4 style="color:#283618;font-family:Times-New-Roman"><b>Want to meet brands that match your aesthetics?</b></h4>
            <p class="card-text" style="color:#e3d5ca">Collaborate with brands to create great content and build your fan base. We help you manage this collaboration so that you can focus on letting your creative juices flow and we take care of the rest.</p>
        </div>
      </div>
      <div class="card" style="width: 18rem; margin-left:10px;border-radius:10px">
        <img class="card-img-top" src="https://img.freepik.com/free-vector/people-shopping-with-bags_24908-56770.jpg?size=626&ext=jpg&ga=GA1.1.415220518.1686658996&semt=ais_user" alt="Card image cap">
        <div class="card-body">
          <h4 style="color:#283618;font-family:Times-New-Roman"> <b>HOW WE WORK Discover Campaigns</b></h4>
            <p class="card-text" style="color:#e3d5ca">Explore brands looking for you to share some love on Youtube, Twitter, Facebook, Instagram and Blogs Apply forCampaigns
              The camaign deliverables along with price based on your profile will be mentioned for each campaign. Apply for the campaigns that interest you with a click of a button.</p>
        </div>
      </div>
      <div class="card" style="width: 18rem; margin-left:10px;border-radius:10px">
        <img class="card-img-top" src="https://img.freepik.com/free-vector/cartoon-working-day-scene-illustration_23-2148958208.jpg?ga=GA1.1.415220518.1686658996&semt=ais_user" alt="Card image cap">
        <div class="card-body">
          <h4 style="color:#283618;font-family:Times-New-Roman"> <b>Create Content And Get Instant Payment</b></h4>
            <p class="card-text" style="color:#e3d5ca">Once you and the brand are in sync, create cool content based on the brief and submit for approval. Once the brand approves the content, share the awesome work with your followers.
              Influencers can now receive Instant Payment after each campaign with a combination of technological and financial options.
            </p>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'HomeView',
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color:#f5ebe0 ;
}

.content {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.card-container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.card {
  background-color: #9f7e69;
  border-radius: 18px;
  color: white;
}

.card-body {
  background-color: #9f7e69;
  border-radius: 10px;
  padding: 20px;
}
</style>