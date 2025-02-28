"""Constants."""

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

GetUsageReadsForDayAndHourQuery = """
query GetUsageReadsForDayAndHour(
	$customerURN: ID
	$timeInterval: TimeInterval
	$resolution: ReadResolution
	$forceLegacyData: Boolean
	$aliased: Boolean
	$saUuid: String
	$spUuid: String
) {
	billingAccountByAuthContext(
		singlePremise: $customerURN
		forceLegacyData: $forceLegacyData
	) {
		serviceAgreementsConnection(
			onlyActive: true
			aliased: $aliased
			matching: $saUuid
		) {
			edges {
				node {
					uuid
					serviceType
					servicePointsConnection(matching: $spUuid) {
						edges {
							node {
								serviceType
								utilityId
								uuid
								readStreams(
									timeInterval: $timeInterval
									readResolution: $resolution
								) {
									timeInterval
									netUsage {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											isPeakPeriod
											__typename
										}
										__typename
									}
									energyDelivered {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									reactiveEnergyDelivered {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									energyReceived {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									demand {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											isMaximum
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									reactivePower {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									apparentPower {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									powerFactor {
										serviceQuantityIdentifier
										unit
										isOpowerDerived
										registerId
										reads {
											readType
											timeInterval
											measuredAmount {
												unit
												value
												__typename
											}
											__typename
										}
										__typename
									}
									__typename
								}
								__typename
							}
							__typename
						}
						__typename
					}
					__typename
				}
				__typename
			}
			__typename
		}
		__typename
	}
}
"""

GetBillingAccountsQuery = """
query GetBillingAccounts(
	$urns: [ID!]
	$first: Int
	$after: String
	$onlyActive: Boolean
	$uheaToken: String
) {
	billingAccountsConnection(byURNs: $urns, first: $first, after: $after) {
		edges {
			node {
				serviceAgreementsConnection(first: 100, onlyActive: $onlyActive) {
					edges {
						node {
							name
							nickname
							urn
							uuid
							serviceType
							utilityId
							utilityCode
							servicePointsConnection(matching: $uheaToken, first: 100) {
								edges {
									node {
										name
										serviceType
										urn
										uuid
										utilityId
										premise {
											mappedSite {
												customer {
													id
													uuid
												}
											}
											timeZone
											name
											uuid
											urn
											utilityId
											address {
												addressLines
												locality
												adminArea
												postalCode
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
"""