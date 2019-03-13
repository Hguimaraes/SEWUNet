---
layout: default
title:  "Paper results"
date:   2019-03-12 00:00:00
categories: main
---

# Speech Enhancement Task

**tl;dr**: Check the full paper [here]().

## On the test-set snippets

Those examples were retrieved from the LibriSpeech (**train-clean-100**) snippets of 2^16 samples used to test the efficiency of the network. In the next section you can find about the model network applied on multiple SNR intervals and with full temporal-context (complete audio files). Just a quick remainder that the Network was trained on noisy signals with an SNR of 5db-15db.

<table>
  <tr>
    <th>Noisy Signal</th>
    <th>Our Method</th>
    <th>Ground Truth</th>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/00FWQOXLMACK5HE_mixture.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/00FWQOXLMACK5HE_separated.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/00FWQOXLMACK5HE_clean.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/X1FTBNP0UX6MUAV_mixture.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/X1FTBNP0UX6MUAV_separated.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/X1FTBNP0UX6MUAV_clean.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/K0W0Q6V9E4OA96B_mixture.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/K0W0Q6V9E4OA96B_separated.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/sewunet_test/K0W0Q6V9E4OA96B_clean.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
</table>


## On Long temporal context

Here we apply our method to more diverse audios on the full length. The results of this evaluation is applied on ASR algorithms to check if there are performance gains.

### SNR between 10db-20db

<table>
  <tr>
    <th>Noisy Signal</th>
    <th>Our Method</th>
    <th>Ground Truth</th>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/2300-131720-0040_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/2300-131720-0040_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/2300-131720-0040.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/3570-5695-0012_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/3570-5695-0012_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/3570-5695-0012.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/5639-40744-0040_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/5639-40744-0040_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/5639-40744-0040.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/7729-102255-0027_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/7729-102255-0027_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/7729-102255-0027.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/61-70970-0037_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/61-70970-0037_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/10db_20db/61-70970-0037.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
</table>

### SNR between 5db-15db

<table>
  <tr>
    <th>Noisy Signal</th>
    <th>Our Method</th>
    <th>Ground Truth</th>
  </tr>
  <tr>
    <td>
      <audio controls style="width: 215px;">
        <source src="{{ site.baseurl }}/assets/results/5db_15db/260-123286-0022_noisy.wav" type="audio/wav">
      </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/260-123286-0022_processed.wav" type="audio/wav">
        </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/260-123286-0022.wav" type="audio/wav">
        </audio>
    </td>
  </tr>
  <tr>
    <td>
      <audio controls style="width: 215px;">
        <source src="{{ site.baseurl }}/assets/results/5db_15db/3729-6852-0028_noisy.wav" type="audio/wav">
      </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/3729-6852-0028_processed.wav" type="audio/wav">
        </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/3729-6852-0028.wav" type="audio/wav">
        </audio>
    </td>
  </tr>
  <tr>
    <td>
      <audio controls style="width: 215px;">
        <source src="{{ site.baseurl }}/assets/results/5db_15db/4507-16021-0051_noisy.wav" type="audio/wav">
      </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/4507-16021-0051_processed.wav" type="audio/wav">
        </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/4507-16021-0051.wav" type="audio/wav">
        </audio>
    </td>
  </tr>
  <tr>
    <td>
      <audio controls style="width: 215px;">
        <source src="{{ site.baseurl }}/assets/results/5db_15db/5683-32866-0019_noisy.wav" type="audio/wav">
      </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/5683-32866-0019_processed.wav" type="audio/wav">
        </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/5683-32866-0019.wav" type="audio/wav">
        </audio>
    </td>
  </tr>
  <tr>
    <td>
      <audio controls style="width: 215px;">
        <source src="{{ site.baseurl }}/assets/results/5db_15db/8224-274384-0006_noisy.wav" type="audio/wav">
      </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/8224-274384-0006_processed.wav" type="audio/wav">
        </audio>
    </td>
    <td>
        <audio controls style="width: 215px;">
          <source src="{{ site.baseurl }}/assets/results/5db_15db/8224-274384-0006.wav" type="audio/wav">
        </audio>
    </td>
  </tr>
</table>

### SNR between 0db-10db

<table>
  <tr>
    <th>Noisy Signal</th>
    <th>Our Method</th>
    <th>Ground Truth</th>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/4507-16021-0059_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/4507-16021-0059_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/4507-16021-0059.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/5639-40744-0024_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/5639-40744-0024_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/5639-40744-0024.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/6930-76324-0019_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/6930-76324-0019_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/6930-76324-0019.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/8463-294825-0019_noisy.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/8463-294825-0019_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/8463-294825-0019.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
  <tr>
    <td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/3575-170457-0034.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/3575-170457-0034_processed.wav" type="audio/wav">
  		</audio>
	</td>
	<td>
    	<audio controls style="width: 215px;">
  			<source src="{{ site.baseurl }}/assets/results/0db_10db/3575-170457-0034.wav" type="audio/wav">
  		</audio>
	</td>
  </tr>
</table>

## ASR Evaluation

@TODO