<template>
  <div class="card2-container">
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">VIEW OUR CASESTUDY</h2>
    <div class="case-study-cards">
      <div class="case-study-card" v-for="caseStudy in caseStudies" :key="caseStudy.id">
        <img :src="caseStudy.image" alt="Case Study Image" class="case-study-image">
        <div class="case-study-content">
          <p style="font-size:15px;background-color:#219ebc;text-align:center;font-style: italic">
            <h3 style="background-color:#219ebc"><strong>{{ caseStudy.campaignName }}</strong></h3>{{ caseStudy.campaignDescription }}</p>
          <div class="case-study-stats" style="background-color:#d8e2dc">
            <div class="stat">
              <p style="font-size:12px">Influencers</p>
              <p><strong>{{ caseStudy.influencers }}</strong></p>
            </div>
            <div class="stat">
              <p style="font-size:12px">Engagement</p>
              <p><strong>{{ caseStudy.engagement }}</strong></p>
            </div>
            <div class="stat">
              <p style="font-size:12px">Impressions</p>
              <p><strong>{{ caseStudy.impressions }}</strong></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CaseStudyCards',
  data() {
    return {
      caseStudies: [
        {
          id: 1,
          image: 'https://images.pexels.com/photos/994234/pexels-photo-994234.jpeg?auto=compress&cs=tinysrgb&w=600',
          campaignName: ' # Fashion World',
          campaignDescription: 'H & M',
          influencers: '1500',
          engagement: '50 K+',
          impressions: '1M+',
        },
        {
          id: 2,
          image: 'https://www.financialexpress.com/wp-content/uploads/2023/03/Yourararaph-text-2023-03-31T133430.218.jpg',
          campaignName: '#Say Cheers to India',
          campaignDescription: 'Dairy Milk',
          influencers: '150',
          engagement: '60K+',
          impressions: '1.5 M+',
        },
        {
          id: 3,
          image: 'https://i.ytimg.com/vi/a5_3OFjGn-A/maxresdefault.jpg',
          campaignName: '#Making Music',
          campaignDescription: 'boAT',
          influencers: '2000',
          engagement: '1.35 M+' ,
          impressions: '2 M+',
        },
        // Add more case studies here
      ],
    };
  },
};
</script>

<style scoped>
.card2-container {
  padding: 20px;
}
.case-study-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.case-study-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  width: calc(33.333% - 20px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.case-study-image {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
.case-study-content {
  padding: 15px;
}
.case-study-stats {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}
.stat {
  text-align: center;
}
</style>