<template>
 <ul class="news__list">
    <form  @submit.prevent="searchNews" class="d-flex flex-column justify-content-center">
        <div class="input-group mx-sm-3 mb-2">
            <label class="visually-hidden" for="search">Search</label>
            <input type="search" name="searchmake" v-model="searchTerm"
                id="search" class="form-control mb-2 mr-sm-2" placeholder="Make" />
            <input type="search" name="searchmodel" v-model="searchTerm"
                id="search" class="form-control mb-2 mr-sm-2" placeholder="Model" />
                <button class="btn btn-primary mb-2">Search</button>
        </div>     
 </form>
 </ul>
</template>

<script>
</script>

<style>
</style>
